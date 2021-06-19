from youtube2notion.youtube2notion import Youtube2notion
from flask import Flask, request
from shutil import rmtree

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

    if not video_id:
        return {'msg': 'invalid video_id'}, 400

    output_dir = './tmp/%s/' % video_id

    y2n = Youtube2notion(
        video_id=video_id,
        output_dir=output_dir,
        notion_token_v2=notion_token_v2,
        notion_page_url=notion_page_url)

    try:
        y2n.execute()
    except Exception as e:
        return {'msg': type(e).__name__ + str(e)}, 400
    finally:
        rmtree(output_dir)

    return {}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
