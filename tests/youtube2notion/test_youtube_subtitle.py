import unittest
from youtube2notion.youtube_subtitle import YoutubeSubtitle
from youtube_transcript_api._errors import NoTranscriptFound


class TestYoutubeSubtitle(unittest.TestCase):

    def setUp(self):
        import warnings
        warnings.filterwarnings(
            "ignore",
            category=ResourceWarning,
            message="unclosed.*<ssl.SSLSocket.*>")

        self.video_id = '5oNcoj4G0xc'

    def test_get_subtitle_elements(self):
        self.assertIsNotNone(
            YoutubeSubtitle.get_subtitle_elements(self.video_id))

    def test_get_subtitle_with_specific_language(self):
        self.assertIsNotNone(
            YoutubeSubtitle.get_subtitle_elements(self.video_id, ['ko', 'en']))
        self.assertIsNotNone(
            YoutubeSubtitle.get_subtitle_elements(self.video_id,
                                                  ['aa', 'bb', 'en']))

    def test_get_subtitle_with_unknown_language_codes_exception(self):
        with self.assertRaises(NoTranscriptFound):
            YoutubeSubtitle.get_subtitle_elements(self.video_id, ['aa', 'bb'])
