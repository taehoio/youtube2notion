from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound


class SubtitleElement:

    def __init__(self, text: str, start: float, duration: float):
        self._text = text
        self._start = start
        self._duration = duration

    @property
    def text(self):
        return self._text

    @property
    def start(self):
        return self._start

    @property
    def duration(self):
        return self._duration


class YoutubeSubtitle:

    @classmethod
    def __fetch_transcript(cls,
                           video_id: str,
                           language_codes: list[str] = ['ko', 'en']) -> list:
        """
        Returns a fetched transcript from YouTube. It makes the best effort to
        get a proper transcript following below priorities:
        1. a manually created transcript prior to a auto-generated one.
        2. language codes in language_codes param will be traversed in order.
        3. if there is neither created nor generated transcript, it will try to
        get a auto-translated one by the first language code of
        language_codes param.
        """
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        try:
            return transcript_list.find_manually_created_transcript(
                language_codes).fetch()
        except NoTranscriptFound:
            pass

        try:
            return transcript_list.find_generated_transcript(
                language_codes).fetch()
        except NoTranscriptFound:
            pass

        if transcript_list and language_codes:
            for transcript in transcript_list:
                return transcript.translate(language_codes[0]).fetch()

    @classmethod
    def get_subtitle_elements(
        cls,
        video_id: str,
        language_code_candidates: list[str] = ['ko', 'en']
    ) -> list[SubtitleElement]:
        fetched_transcript = YoutubeSubtitle.__fetch_transcript(
            video_id, language_code_candidates)

        subtitle_elements: list[SubtitleElement] = []
        for sentence in fetched_transcript:
            subtitle_elements.append(
                SubtitleElement(
                    text=sentence.get('text'),
                    start=sentence.get('start'),
                    duration=sentence.get('duration')))

        return subtitle_elements
