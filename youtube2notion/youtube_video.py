from yt_dlp import YoutubeDL


class YoutubeVideo:

    FORMAT_CODE = '134'
    """
    youtube video format code 134

    extention: mp4
    resolution: 640x360
    note: 360p, 87k , mp4_dash container, avc1.4d401e@  87k, 25fps, video only
    """

    @classmethod
    def download(cls, video_id: str, output_dir: str = '') -> str:
        output_filename: str = YoutubeVideo.get_output_filename(
            video_id, output_dir, '.mp4')

        ydl_opts = {
            'quiet': True,
            'format': cls.FORMAT_CODE,
            'writethumbnail': True,
            'writeinfojson': True,
            'outtmpl': output_filename,
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([YoutubeVideo.to_url(video_id)])

        return output_filename

    @staticmethod
    def get_output_filename(video_id: str,
                            output_dir: str,
                            extention: str = '.mp4') -> str:
        return output_dir + video_id + extention

    @staticmethod
    def to_url(video_id: str) -> str:
        return 'https://youtu.be/' + video_id
