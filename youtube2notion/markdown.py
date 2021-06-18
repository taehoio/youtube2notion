from youtube2notion.youtube_subtitle import SubtitleElement


class Markdown:

    @classmethod
    def generate(cls, title: str, subtitle_elements: list[SubtitleElement],
                 images_dir: str) -> str:
        md = ''
        md += '# ' + title + '\n'
        md += '\n'

        for element in subtitle_elements:
            md += '![](' + images_dir + 'image_%(sec)05d' % {
                'sec': int(element.start + (element.duration / 2))
            } + '.jpeg)'
            md += '\n\n'
            md += element.text + '\n'
            md += '\n'

        return md
