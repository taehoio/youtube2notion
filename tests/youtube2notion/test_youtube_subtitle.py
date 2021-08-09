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

        self.video_id = '5oNcoj4G0xc'

    def test_get_subtitle_elements(self):
        self.assertIsNotNone(
            YoutubeSubtitle.get_subtitle_elements(self.video_id))

    def test_with_manually_created_subtitle(self):
        self.assertIsNotNone(
            YoutubeSubtitle.get_subtitle_elements('MY5SatbZMAo', ['en']))

    def test_with_auto_generated_subtitle(self):
        self.assertIsNotNone(
            YoutubeSubtitle.get_subtitle_elements('5-MXyCr3y5M', ['ko']))

    def test_with_auto_translated_subtitle(self):
        self.assertIsNotNone(
            YoutubeSubtitle.get_subtitle_elements('5-MXyCr3y5M', ['en']))

    def test_with_translation_language_not_available_exception(self):
        with self.assertRaises(TranslationLanguageNotAvailable):
            YoutubeSubtitle.get_subtitle_elements(self.video_id, ['aa', 'bb'])
