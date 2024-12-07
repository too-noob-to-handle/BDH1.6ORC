#!/usr/bin/env python3

import os
import subprocess
import shutil
import glob
import pathlib
import time

# Paths
FILE_DIRECTORY = pathlib.Path(__file__).parent.absolute()
TEMPORARY_PATH = os.path.join(FILE_DIRECTORY, "cache")
OUTPUT_PATH = os.path.join(FILE_DIRECTORY, "output")
UTILS = os.path.join(FILE_DIRECTORY, "utils")
TAG = "JoyBangla"

# Headers
HEADERS = (
    '-H "country-code: QkQ%3D" '
    '-H "Host: vodmprod-cdn.toffeelive.com" '
    '-H "Cookie: _fbp=fb.1.1730886642455.230583548137401120; '
    '_ga=GA1.1.56081587.1730886643; '
    'Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly92b2RtcHJvZC1jZG4udG9mZmVlbGl2ZS5jb20v:Expires=1742474615:KeyName=prod_vod:Signature=4vlmgUa0jcyPkU8uFhEG3d99Fwg0IRWF4HLddEP6GC8vqQ_arU9uTgU4ydHkQF4W9OnFVcYnJkx8FfNh1msiDg; '
    '_ga_02M4D9SN5F=GS1.1.1733379633.5.1.1733379672.0.0.0" '
    '-H "TOFFEE-SESSION-TOKEN: VnpYF/MvBnRqvkOF4Rh0yM5Z4oUoDEEIEoI/E7Q1Y13nugYQtxm1ScOwjzMedU9Ga+QXMCX7dIS+A0qVtrM1Blh4bDWgHrBBcEoaK7vf+et/KijNRsaFP5KUZycs6mj6YSzc/R0tS6BoVHluVejm19oc4ZlVNnx+TsZ5/qiWfqg=" '
    '-H "User-Agent: Toffee/6.0.2 (Linux;Android 13) AndroidXMedia3/1.1.1/58262915/af7b95851941da4a"'
)

# Utility Functions
def divider():
    """Print a divider line."""
    print('-' * shutil.get_terminal_size().columns)

def empty_folder(folder):
    """Empty the given folder."""
    files = glob.glob(f'{folder}/*')
    for f in files:
        os.remove(f)
    print("Emptied Temporary Files!")
    divider()

def run_command(command):
    """Run a command using subprocess."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
        divider()

def download_video(resolution, mpd_url, temp_file, output_file, intro_file):
    """Download and process a video."""
    print(f"Downloading {resolution} video from CDN...")
    command = (
        f'"{os.path.join(UTILS, "N_m3u8DL-RE")}" -sv res="{resolution}*" {mpd_url} '
        f'--tmp-dir "{TEMPORARY_PATH}" --save-dir "{TEMPORARY_PATH}" '
        f'--binary-merge false --ffmpeg-binary-path /usr/bin/ffmpeg '
        f'--save-name "{temp_file}" --del-after-done --log-level INFO {HEADERS}'
    )
    run_command(command)

    print(f"Merging {resolution} video with intro and subtitle...")

    # Verify if intro file exists
    if not os.path.exists(intro_file):
        print(f"Error: Intro file not found: {intro_file}")
        return

    mkvmerge_command = (
        f'"{os.path.join(UTILS, "mkvmerge")}" --output "{os.path.join(OUTPUT_PATH, output_file)}-{TAG}.mkv" '
        f'--language 0:bn --track-name "0:Join Us - @JoyBangla4U" '
        f'--language 1:bn --track-name "1:Join Us - @JoyBangla4U" '
        f'"(" "{intro_file}" ")" + "(" "{os.path.join(TEMPORARY_PATH, temp_file)}.mp4" ")" '
        f'--language 0:und --track-name "0:Join Us - @JoyBangla4U" '
        f'"(" "{os.path.join(UTILS, "ZGH596AF1426AF58623AGVH.srt")}" ")" '
        f'--title "Join Us - @JoyBangla4U" --track-order 0:0,0:1,2:0 '
        f'--append-to 1:0:0:0,1:1:0:1'
    )
    run_command(mkvmerge_command)

def drive_upload():
    """Upload the output files to cloud storage."""
    divider()
    print("Uploading... (Takes some time)")
    time.sleep(2)
    rclone_config = os.path.join(UTILS, "rclone.conf")

    for target in ["onedrive:BUP", "mega:Uploads"]:
        command = f'"{os.path.join(UTILS, "rclone")}" --config="{rclone_config}" copy "{OUTPUT_PATH}" "{target}"'
        run_command(command)

    print("Cloud uploads complete!")

# Main Process
divider()
print("**** BDH-DL by JoyBangla ****")
divider()

# Get Input
MPD_URL = input("Enter NonDRM m3u8/Direct Stream URL: \n> ")
FILENAME_1080 = input("Enter 1080p FileName: ")
divider()
FILENAME_720 = input("Enter 720p FileName: ")
divider()

# Define Intro Files
INTRO_FILE_1080 = os.path.join(UTILS, "44k1080.mkv")
INTRO_FILE_720 = os.path.join(UTILS, "44k720.mkv")

# Download Videos
download_video("1080", MPD_URL, "temp-BDH", FILENAME_1080, INTRO_FILE_1080)
download_video("720", MPD_URL, "temp-BDH2", FILENAME_720, INTRO_FILE_720)

# Upload to Cloud
drive_upload()

divider()
print("Process Finished. Final Video Files are saved in the /output directory.")
divider()

# Cleanup
delete_choice = input("Delete cache files? (y/n)\ny) Yes (default)\nn) No\ny/n> ").strip().lower()
if delete_choice != "n":
    empty_folder(TEMPORARY_PATH)
