from youtube2notion.markdown import Markdown
from youtube2notion.ffmpeg import Ffmpeg
from youtube2notion.youtube_video import YoutubeVideo
from youtube2notion.youtube_subtitle import SubtitleElement, YoutubeSubtitle
from youtube2notion.youtube_info import InformationElement, YoutubeInfo
from pathlib import Path
from notion.client import NotionClient
from notion.block import PageBlock
from md2notion.upload import upload


class Youtube2notion:

    def __init__(self,
                 video_id: str,
                 output_dir: str = '',
                 notion_token_v2: str = '',
                 notion_page_url: str = '',
                 subtitle_language: str = 'ko',
                 info_title: str = '',
                 info_author_name: str = '',
                 info_author_url: str = '',
                 ):
        self.video_id = video_id
        self.output_dir = output_dir
        self.images_output_dir = self.output_dir + 'images/'

        self.notion_token_v2 = notion_token_v2
        self.notion_page_url = notion_page_url

        self.subtitle_language = subtitle_language

        self.info_title = info_title
        self.info_author_name = info_author_name
        self.info_author_url = info_author_url

    def _download_video(self) -> str:
        return YoutubeVideo.download(self.video_id, self.output_dir)

    def _get_subtitle_elements(self) -> list[SubtitleElement]:
        return YoutubeSubtitle.get_subtitle_elements(self.video_id,
                                                     [self.subtitle_language])

    def _get_info_element(self) -> InformationElement:
        info_element = YoutubeInfo.get_information_element(self.video_id)
        self.info_title = info_element.title
        self.info_author_name = info_element.author_name
        self.info_author_url = info_element.author_url

    def _take_screenshots(self, input_filename: str):
        Path(self.images_output_dir).mkdir(parents=True, exist_ok=True)

        Ffmpeg.take_screenshots(input_filename, self.images_output_dir)

    def _generage_markdown(self, title: str,
                           subtitle_elements: list[SubtitleElement],
                           images_dir: str) -> str:
        return Markdown.generate(
            title,
            subtitle_elements,
            images_dir,
        )

    def _write_markdown_file(self, md: str, output_markdown_filename: str):
        f = open(output_markdown_filename, 'w')
        f.write(md)
        f.close()

    def _should_upload_to_notion(self) -> bool:
        return self.notion_token_v2 and self.notion_page_url

    def _upload_to_notion(self, md_file: str, notion_token_v2: str,
                          notion_page_url: str):
        client = NotionClient(token_v2=notion_token_v2)
        page = client.get_block(notion_page_url)

        with open(md_file, 'r', encoding='utf-8') as f:
            new_page = page.children.add_new(
                PageBlock,
                title=self.info_title + '(' + self.subtitle_language + ')')
            upload(f, new_page)

    def execute(self):
        subtitle_elements = self._get_subtitle_elements()
        self._get_info_element()

        downloaded_video_filename = self._download_video()
        self._take_screenshots(downloaded_video_filename)

        md = self._generage_markdown(
            title=self.info_title + '(' + self.subtitle_language + ')',
            subtitle_elements=subtitle_elements,
            images_dir='./images/')

        md_filename = self.output_dir + self.video_id + '.md'
        self._write_markdown_file(md, md_filename)

        if self._should_upload_to_notion():
            self._upload_to_notion(
                md_filename,
                notion_token_v2=self.notion_token_v2,
                notion_page_url=self.notion_page_url)
