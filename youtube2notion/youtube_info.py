import requests


class InformationElement:

    def __init__(
        self,
        title: str = '',
        author_name: str = '',
        author_url: str = '',
    ):
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
        res = requests.get("https://www.youtube.com/oembed", params=params)

        if res.status_code == 200:
            res_json = res.json()

            return InformationElement(
                title=res_json.get('title'),
                author_name=res_json.get('author_name'),
                author_url=res_json.get('author_url'),
            )
        else:
            return InformationElement(title=video_id)
