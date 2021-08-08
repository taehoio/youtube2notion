from youtube_transcript_api import YouTubeTranscriptApi


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
    def get_subtitle_elements(cls,
                              video_id: str,
                              languages=['ko', 'en']) -> list[SubtitleElement]:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        is_finded = {'first': False, 'second': False}
        for transcript in transcript_list:
            if transcript.language_code == languages[0]:
                is_finded['first'] = True
                break
            if transcript.language_code == languages[1]:
                is_finded['second'] = True

        transcript_result: list[SubtitleElement] = []
        if is_finded['first'] == True:
            transcript_result = transcript.fetch()
        elif is_finded['second'] == True:
            transcript = transcript_list.find_transcript([languages[1]])
            transcript_result = transcript.translate(languages[0]).fetch()
        else:
            transcript_result = transcript.translate(languages[0]).fetch()

        subtitle_elements: list[SubtitleElement] = []
        for sentence in transcript_result:
            subtitle_elements.append(
                SubtitleElement(
                    text=sentence.get('text'),
                    start=sentence.get('start'),
                    duration=sentence.get('duration')))

        return subtitle_elements
