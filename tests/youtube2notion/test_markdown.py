import unittest
from youtube2notion.youtube_subtitle import SubtitleElement
from youtube2notion.markdown import Markdown


class TestMarkdown(unittest.TestCase):

    def test_generate(self):
        title: str = 'Hello, World!'
        subtitle_elements: list[SubtitleElement] = [
            SubtitleElement(text='hi', start=12.34, duration=0.567),
            SubtitleElement(text='bye', start=45.12, duration=0.890),
        ]
        images_dir: str = './images'

        md = Markdown.generate(
            title=title,
            subtitle_elements=subtitle_elements,
            images_dir=images_dir)

        self.assertEqual(
            md, '''# Hello, World!

![](./imagesimage_00012.jpeg)

hi

![](./imagesimage_00045.jpeg)

bye''')
