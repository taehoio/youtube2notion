import unittest
from youtube2notion.youtube_subtitle import YoutubeSubtitle
from youtube_transcript_api._errors import TranslationLanguageNotAvailable


class TestYoutubeSubtitle(unittest.TestCase):

    def setUp(self):
        import warnings
        warnings.filterwarnings(
            "ignore",
            category=ResourceWarning,
            message="unclosed.*<ssl.SSLSocket.*>")

        self.video_id = 'Kc_cvAXCs4Y'

    def test_get_subtitle_elements(self):
        self.assertIsNotNone(
            YoutubeSubtitle.get_subtitle_elements(self.video_id))

    def test_get_subtitle_with_specific_language(self):
        self.assertIsNotNone(
            YoutubeSubtitle.get_subtitle_elements(self.video_id, ['ko', 'en']))

    def test_get_subtitle_with_unknown_language_exception(self):
        with self.assertRaises(TranslationLanguageNotAvailable):
            YoutubeSubtitle.get_subtitle_elements(self.video_id, ['aa', 'bb'])
