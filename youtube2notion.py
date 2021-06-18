from youtube2notion.youtube2notion import Youtube2notion
import click


@click.command()
@click.argument('video_id')
@click.option('--output-dir', '-o', 'output_dir', required=False, type=str)
@click.option(
    '--notion-token-v2', '-t', 'notion_token_v2', required=False, type=str)
@click.option(
    '--notion-page-url', '-p', 'notion_page_url', required=False, type=str)
def youtube2notion(video_id: str, output_dir, notion_token_v2, notion_page_url):
    if not output_dir:
        output_dir = './tmp/%s/' % video_id

    click.echo('video_id: %s' % video_id)
    click.echo('output_dir: %s' % output_dir)
    click.echo('notion_token_v2: %s' % notion_token_v2)
    click.echo('notion_page_url: %s' % notion_page_url)

    y2n = Youtube2notion(
        video_id=video_id,
        output_dir=output_dir,
        notion_token_v2=notion_token_v2,
        notion_page_url=notion_page_url)

    try:
        y2n.execute()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    youtube2notion()
