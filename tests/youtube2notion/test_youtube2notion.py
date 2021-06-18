import unittest
from youtube2notion.youtube2notion import Youtube2notion


class TestYoutube2notion(unittest.TestCase):

    def setUp(self):
        import warnings
        warnings.filterwarnings(
            "ignore",
            category=ResourceWarning,
            message="unclosed.*<ssl.SSLSocket.*>")

        video_id = 'Kc_cvAXCs4Y'
        notion_token_v2 = ''
        notion_page_url = ''

        self.y2n = Youtube2notion(
            video_id=video_id,
            notion_token_v2=notion_token_v2,
            notion_page_url=notion_page_url)

    def test_execute(self):
        self.y2n.execute()
