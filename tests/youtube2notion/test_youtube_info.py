import unittest

from youtube2notion.youtube_info import YoutubeInfo


class TestYoutubeInfo(unittest.TestCase):

    def setUp(self):
        self.video_id = '5oNcoj4G0xc'

    def test_get_information_element(self):
        self.assertIsNotNone(YoutubeInfo.get_information_element(self.video_id))
