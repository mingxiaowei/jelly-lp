import os
import subprocess

def reencode_video(input_file: str, output_file: str) -> None:
    """Reencodes video into h.264 coded format using ffmpeg from a subprocess.

    Args:
        input_file: abspath to existing video
        output_file: abspath to to new mp4 video using h.264 codec

    """
    # check input file exists
    assert os.path.isfile(input_file), 'input video does not exist.'
    # check directory for saving outputs exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    # create ffmpeg command
    ffmpeg_cmd = f'ffmpeg -i {input_file} -c:v libx264 -pix_fmt yuv420p -c:a copy -y {output_file}'
    # run command
    subprocess.run(ffmpeg_cmd, shell=True)

INPUT_FILE = "/home/mingxiao/Desktop/jellyfish/video/full_video_4.avi"
OUTPUT_FILE = "/home/mingxiao/Desktop/jellyfish/video/full_video_4.mp4"

if __name__ == "__main__":
    reencode_video(INPUT_FILE, OUTPUT_FILE)