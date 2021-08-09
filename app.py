from youtube2notion.youtube2notion import Youtube2notion
from flask import Flask, request
from os.path import exists
from shutil import rmtree
from os import environ
import googlecloudprofiler

app = Flask(__name__)


@app.route('/')
def index():
    return {}


@app.route('/upload', methods=['POST'])
def upload():
    req = request.get_json()
    video_id = req.get('video_id')
    notion_token_v2 = req.get('notion_token_v2')
    notion_page_url = req.get('notion_page_url')
    subtitle_language = req.get('subtitle_language')

    if not video_id:
        return {'msg': 'invalid video_id'}, 400

    output_dir = './tmp/%s/' % video_id

    y2n = Youtube2notion(
        video_id=video_id,
        output_dir=output_dir,
        notion_token_v2=notion_token_v2,
        notion_page_url=notion_page_url,
        subtitle_language=subtitle_language)

    try:
        y2n.execute()
    except Exception as e:
        return {'msg': type(e).__name__ + str(e)}, 400
    finally:
        if exists(output_dir):
            rmtree(output_dir)

    return {}


def shouldProfile() -> bool:
    return environ.get('SHOULD_PROFILE') == 'true'


def setUpProfiler(serviceName: str):
    googlecloudprofiler.start(service=serviceName)


def main():
    serviceName: str = 'youtube2notion'

    if shouldProfile():
        setUpProfiler(serviceName)

    app.run(host='0.0.0.0', port='5000', debug=True)


if __name__ == "__main__":
    main()
