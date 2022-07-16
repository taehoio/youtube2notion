import requests


class InformationElement:

    def __init__(self, title: str, author_name: str, author_url: str):
        self._title = title
        self._author_name = author_name
        self._author_url = author_url

    @property
    def title(self):
        return self._title

    @property
    def author_name(self):
        return self._author_name

    @property
    def author_url(self):
        return self._author_url


class YoutubeInfo:

    @classmethod
    def get_information_element(cls, video_id: str) -> InformationElement:

        params = {
            "format": "json",
            "url": "https://www.youtube.com/watch?v=%s" % video_id
        }
        res = requests.get(
            "https://www.youtube.com/oembed", params=params).json()

        information_element = InformationElement(
            title=res.get('title'),
            author_name=res.get('author_name'),
            author_url=res.get('author_url'),
        )
        return information_element
