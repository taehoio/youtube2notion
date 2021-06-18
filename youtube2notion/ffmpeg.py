import subprocess


class Ffmpeg:

    @classmethod
    def take_screenshots(cls, input_filename: str, output_dir: str = ''):
        cmd_args = [
            'ffmpeg',
            '-hide_banner',
            '-v',
            'quiet',
            '-stats'
            '-i',
            input_filename,
            '-vf',
            'fps=1/1',    # every second. e.g. every minite is 'fps=1/60'
            output_dir + 'image_%05d.jpeg',
        ]

        subprocess.call(cmd_args)
