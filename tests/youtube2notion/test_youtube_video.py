import unittest
from youtube2notion.youtube_video import YoutubeVideo
from os.path import isfile


class TestYoutubeVideo(unittest.TestCase):

    def setUp(self):
        self.video_id = 'Kc_cvAXCs4Y'

    def test_get_output_filename(self):
        self.assertEqual(
            YoutubeVideo.get_output_filename(self.video_id,
                                             './tmp/%s/' % self.video_id),
            './tmp/Kc_cvAXCs4Y/Kc_cvAXCs4Y.mp4')

    def test_to_url(self):
        self.assertEqual(
            YoutubeVideo.to_url(self.video_id), 'https://youtu.be/Kc_cvAXCs4Y')

    def test_download(self):
        downloaded_video_filename = YoutubeVideo.download(
            video_id=self.video_id,
            output_dir=YoutubeVideo.get_output_filename(
                self.video_id, './tmp/%s/' % self.video_id))

        self.assertTrue(isfile(downloaded_video_filename))
