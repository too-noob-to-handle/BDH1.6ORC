#@title Binge DL

#!/usr/bin/env python3

import os
import subprocess
import shutil
import glob
import pathlib
import platform
import time

# Paths
FILE_DIRECTORY=str(pathlib.Path(__file__).parent.absolute())
TEMPORARY_PATH = FILE_DIRECTORY+"/cache"
OUTPUT_PATH = FILE_DIRECTORY+"/output"
UTILS = FILE_DIRECTORY+"/utils"
TAG = "JoyBangla
Authorize = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJGcmVlIiwiY3JlYXRlZEF0IjoiY3JlYXRlIGRhdGUiLCJ1cGRhdGVkQXQiOiJ1cGRhdGUgZGF0ZSIsInR5cGUiOiJ0b2tlbiIsImRldlR5cGUiOiJ3ZWIiLCJleHRyYSI6IjMxNDE1OTI2IiwiaWF0IjoxNzEwNzg3NDM1LCJleHAiOjE3MTA5NjAyMzV9.IqBGKb2kTyzfjQhFsno1L3CSPvNg6uW3WtJ4HJen6Ps"

def divider():
    print ('-' * shutil.get_terminal_size().columns)

def empty_folder(folder):
    files = glob.glob('%s/*'%folder)
    for f in files:
        os.remove(f)
    print("Emptied Temporary Files!")
    divider()
    quit()

def download_drm_content(mpd_url):
    divider()
    print("Processing Video Info..")
    divider()
    KEY = input("ENTER Key: ")
    divider()
    FILENAME = input("ENTER FileName: ")

    divider()
    print("Downloading Video from CDN..")
    os.system(f'wget -O {TEMPORARY_PATH}/unlock.key {KEY} --header="Authorization: {Authorize}" --header="Host: ss.binge.buzz" --header="User-Agent: Exoplayer" && {UTILS}/N_m3u8DL-RE -sv best {mpd_url} --custom-hls-key "{TEMPORARY_PATH}/unlock.key" --tmp-dir "{TEMPORARY_PATH}" --save-dir "{TEMPORARY_PATH}" --save-name "temp-BDH" -H "Host: ott.bingebd.com" -H "os-type: android" -H "Authorization: {Authorize}" -H "User-Agent: Exoplayer" --del-after-done --log-level OFF &&  mkvmerge --output "{OUTPUT_PATH}/{FILENAME}-{TAG}.mkv" --track-name "0:Join Us - @JoyBangla4U" --track-name "1:Join Us - @JoyBangla4U" \'(\' {TEMPORARY_PATH}/temp-BDH.mp4 \')\' --track-name "0:Join Us - @JoyBangla4U" \'(\' /content/ZGH596AF1426AF58623AGVH.srt \')\' --title "Join Us - @JoyBangla4U" --track-order 0:0,0:1,1:0 ')

def drive_upload():
    divider()
    print("Uploading.. (Takes some time)")
    time.sleep(2)
    os.system(f'{UTILS}/rclone --config={UTILS}/rclone.conf copy "{OUTPUT_PATH}" "onedrive:BUP"')
    time.sleep(2)
    os.system(f'{UTILS}/rclone --config={UTILS}/rclone.conf copy "{OUTPUT_PATH}" "mega:Uploads"')
    print("Gdrive Upload Complete!")

divider()
print("**** BDH-DL by JoyBangla ****")
divider()
MPD_URL = input("Enter NonDRM m3u8/Direct Stream URL: \n> ")
download_drm_content(MPD_URL)
drive_upload()
divider()
print("Process Finished. Final Video File is saved in /output directory.")
divider()

delete_choice = input("Delete cache files? (y/n)\ny) Yes (default)\nn) No\ny/n> ")

if delete_choice == "n":
    divider()
else:
    #empty_folder(TEMPORARY_PATH)
    os.system(f'rm -r "{TEMPORARY_PATH}" && mkdir "{TEMPORARY_PATH}"')
