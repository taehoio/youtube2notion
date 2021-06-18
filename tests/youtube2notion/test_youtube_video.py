import unittest
from youtube2notion.youtube_video import YoutubeVideo


class TestYoutubeVideo(unittest.TestCase):

    def setUp(self):
        self.video_id = 'MB5IX-np5fE'

    def test_get_output_filename(self):
        self.assertEqual(
            YoutubeVideo.get_output_filename(self.video_id, './tmp/'),
            './tmp/MB5IX-np5fE.mp4')

    def test_to_url(self):
        self.assertEqual(
            YoutubeVideo.to_url(self.video_id), 'https://youtu.be/MB5IX-np5fE')

    def test_download(self):
        YoutubeVideo.download(
            video_id=self.video_id,
            output_dir=YoutubeVideo.get_output_filename(self.video_id,
                                                        './tmp/'))
