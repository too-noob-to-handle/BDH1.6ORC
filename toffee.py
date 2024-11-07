#@title Tofee DL 1080p & 720p Both

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
INTRO_PATH = FILE_DIRECTORY
SUB = FILE_DIRECTORY
TAG = "JoyBangla"

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
    FILENAME = input("ENTER 1080p FileName: ")
    divider()
    FILENAME2 = input("ENTER 720p FileName: ")
    divider()
    print("Downloading 1st Video from CDN..")
    os.system(f'{UTILS}/N_m3u8DL-RE -sv res="1080*" {mpd_url} --tmp-dir "{TEMPORARY_PATH}" --save-dir "{TEMPORARY_PATH}" --binary-merge true --ffmpeg-binary-path /usr/bin/ffmpeg --save-name "temp-BDH" -H "country-code: QkQ%3D" -H "Host: vodmprod-cdn.toffeelive.com" -H "TOFFEE-SESSION-TOKEN: VnpYF/MvBnRqvkOF4Rh0yM5Z4oUoDEEIEoI/E7Q1Y13nugYQtxm1ScOwjzMedU9Ga+QXMCX7dIS+A0qVtrM1Blh4bDWgHrBBcEoaK7vf+et/KijNRsaFP5KUZycs6mj6YSzc/R0tS6BoVHluVejm19oc4ZlVNnx+TsZ5/qiWfqg=" -H "Cookie: Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly92b2RtcHJvZC1jZG4udG9mZmVlbGl2ZS5jb20v:Expires=1732473690:KeyName=prod_vod:Signature=mMDavx3T5meVE3HfVEPMDsqVkiA04eRmZWWsIFGvdeElqt1Hr8TtwKLDBqYSzk7KzABm5yx7BAGzcp6pXCnmCA" -H "User-Agent: Toffee/6.0.2 (Linux;Android 13) AndroidXMedia3/1.1.1/58262915/af7b95851941da4a" --del-after-done --log-level INFO && ffmpeg -i "{TEMPORARY_PATH}/temp-BDH.ts" -c:v copy -c:a copy "{TEMPORARY_PATH}/temp-BDH.mp4" && rm {TEMPORARY_PATH}/temp-BDH.ts && mkvmerge --output "{OUTPUT_PATH}/{FILENAME}-{TAG}.mkv" --track-name "0:Join Us - @JoyBangla4U" --track-name "1:Join Us - @JoyBangla4U" "{INTRO_PATH}/48k1080.mkv" + "{TEMPORARY_PATH}/temp-BDH.mp4" --language 0:en --language 1:en --track-name "0:Join Us - @JoyBangla4U" \'(\' {SUB}/ZGH596AF1426AF58623AGVH.srt \')\' --title "Join Us - @JoyBangla4U" --track-order 0:0,0:1,0:2,1:0,1:1,1:2 &&  rm {TEMPORARY_PATH}/temp-BDH.mp4')
    print("Downloading 2nd Video from CDN..")
    time.sleep(2)
    os.system(f'{UTILS}/N_m3u8DL-RE -sv res="720*" {mpd_url} --tmp-dir "{TEMPORARY_PATH}" --save-dir "{TEMPORARY_PATH}" --binary-merge true --ffmpeg-binary-path /usr/bin/ffmpeg --save-name "temp2-BDH" -H "country-code: QkQ%3D" -H "Host: vodmprod-cdn.toffeelive.com" -H "TOFFEE-SESSION-TOKEN: VnpYF/MvBnRqvkOF4Rh0yM5Z4oUoDEEIEoI/E7Q1Y13nugYQtxm1ScOwjzMedU9Ga+QXMCX7dIS+A0qVtrM1Blh4bDWgHrBBcEoaK7vf+et/KijNRsaFP5KUZycs6mj6YSzc/R0tS6BoVHluVejm19oc4ZlVNnx+TsZ5/qiWfqg=" -H "Cookie: Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly92b2RtcHJvZC1jZG4udG9mZmVlbGl2ZS5jb20v:Expires=1732473690:KeyName=prod_vod:Signature=mMDavx3T5meVE3HfVEPMDsqVkiA04eRmZWWsIFGvdeElqt1Hr8TtwKLDBqYSzk7KzABm5yx7BAGzcp6pXCnmCA" -H "User-Agent: Toffee/6.0.2 (Linux;Android 13) AndroidXMedia3/1.1.1/58262915/af7b95851941da4a" --del-after-done --log-level INFO && ffmpeg -i "{TEMPORARY_PATH}/temp-BDH2.ts" -c:v copy -c:a copy "{TEMPORARY_PATH}/temp-BDH2.mp4" && rm {TEMPORARY_PATH}/temp-BDH2.ts && mkvmerge --output "{OUTPUT_PATH}/{FILENAME2}-{TAG}.mkv" --track-name "0:Join Us - @JoyBangla4U" --track-name "1:Join Us - @JoyBangla4U" "{INTRO_PATH}/48k720.mkv" + "{TEMPORARY_PATH}/temp-BDH2.mp4" --language 0:en --language 1:en --track-name "0:Join Us - @JoyBangla4U" \'(\' {SUB}/ZGH596AF1426AF58623AGVH.srt \')\' --title "Join Us - @JoyBangla4U" --track-order 0:0,0:1,0:2,1:0,1:1,1:2 && rm {TEMPORARY_PATH}/temp-BDH2.mp4')

def drive_upload():
    divider()
    print("Uploading.. (Takes some time)")
    time.sleep(2)
    os.system(f'rclone --config={UTILS}/rclone.conf copy "{OUTPUT_PATH}" "onedrive:BUP"')
    time.sleep(2)
    os.system(f'rclone --config={UTILS}/rclone.conf copy "{OUTPUT_PATH}" "mega:Uploads"')
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
