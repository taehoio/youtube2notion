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
        transcript = YouTubeTranscriptApi().get_transcript(video_id, languages)

        subtitle_elements: list[SubtitleElement] = []
        for sentence in transcript:
            subtitle_elements.append(
                SubtitleElement(
                    text=sentence.get('text'),
                    start=sentence.get('start'),
                    duration=sentence.get('duration')))

        return subtitle_elements
