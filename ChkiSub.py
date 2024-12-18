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
    SUBURL1 = input("ENTER 1st Subtitle URL: ")
    divider()
    SUBURL2 = input("ENTER 2nd Subtitle URL: ")
    if SUBURL2 == "":
                SUBURL2 = "https://gist.githubusercontent.com/too-noob-to-handle/21f0d81a57ce0a3a163ec9d87335dbd6/raw/ZGH596AF1426AF58623AGVH.srt"
    divider()
    FILENAME = input("ENTER 1st FILENAME: ")
    divider()
    FILENAME2 = input("ENTER 2nd FILENAME: ")
    print("Downloading 1st Video from CDN..")
    os.system(f'wget -O "{TEMPORARY_PATH}/Sub1.srt" "{SUBURL1}" && wget -O "{TEMPORARY_PATH}/Sub2.srt" "{SUBURL2}" && {UTILS}/N_m3u8DL-RE -sv res="1080*" {mpd_url} -H "User-Agent: Dart/3.4 (dart:io)" -H "Accept-Encoding: gzip" -H "vpsid: 417eae185605f2f26e890ab0a316bf9b4af7f5af" -H "Platform: android" -H "Referer: https://www.chorki.com" --tmp-dir "{TEMPORARY_PATH}" --save-dir "{TEMPORARY_PATH}" --binary-merge true --ffmpeg-binary-path /usr/bin/ffmpeg --save-name "temp-BDH" -H "User-Agent: B Player" --del-after-done --log-level ERROR && ffmpeg -i "{TEMPORARY_PATH}/temp-BDH.ts" -c:v copy -c:a copy "{TEMPORARY_PATH}/temp-BDH.mp4" && rm {TEMPORARY_PATH}/temp-BDH.ts && mkvmerge --output "{OUTPUT_PATH}/{FILENAME}-{TAG}.mkv" --track-name "0:Join Us - @JoyBangla4U" --track-name "1:Join Us - @JoyBangla4U" "{INTRO_PATH}/48k1080.mkv" + "{TEMPORARY_PATH}/temp-BDH.mp4" --language 0:en --language 1:en --track-name "0:Join Us - @JoyBangla4U" \'(\' {TEMPORARY_PATH}/Sub1.srt \')\' --track-name "0:Join Us - @JoyBangla4U" \'(\' {TEMPORARY_PATH}/Sub2.srt \')\' --title "Join Us - @JoyBangla4U" --track-order 0:0,0:1,0:2,1:0,1:1,1:2 &&  rm {TEMPORARY_PATH}/temp-BDH.mp4')
    print("Downloading 2nd Video from CDN..")
    time.sleep(2)
    os.system(f'{UTILS}/N_m3u8DL-RE -sv res="720*" {mpd_url} -H "User-Agent: Dart/3.4 (dart:io)" -H "Accept-Encoding: gzip" -H "vpsid: 417eae185605f2f26e890ab0a316bf9b4af7f5af" -H "Platform: android" -H "Referer: https://www.chorki.com" --tmp-dir "{TEMPORARY_PATH}" --save-dir "{TEMPORARY_PATH}" --binary-merge true --ffmpeg-binary-path /usr/bin/ffmpeg --save-name "temp-BDH2" -H "User-Agent: B Player" --del-after-done --log-level ERROR && ffmpeg -i "{TEMPORARY_PATH}/temp-BDH2.ts" -c:v copy -c:a copy "{TEMPORARY_PATH}/temp-BDH2.mp4" && rm {TEMPORARY_PATH}/temp-BDH2.ts && mkvmerge --output "{OUTPUT_PATH}/{FILENAME2}-{TAG}.mkv" --track-name "0:Join Us - @JoyBangla4U" --track-name "1:Join Us - @JoyBangla4U" "{INTRO_PATH}/48k720.mkv" + "{TEMPORARY_PATH}/temp-BDH2.mp4" --language 0:en --language 1:en --track-name "0:Join Us - @JoyBangla4U" \'(\' {TEMPORARY_PATH}/Sub1.srt \')\' --track-name "0:Join Us - @JoyBangla4U" \'(\' {TEMPORARY_PATH}/Sub2.srt \')\' --title "Join Us - @JoyBangla4U" --track-order 0:0,0:1,0:2,1:0,1:1,1:2 && rm {TEMPORARY_PATH}/temp-BDH2.mp4')

VIDEO_ID = "video_avc1"
AUDIO_ID = "audio_und_mp4a"

def drive_upload():
    divider()
    print("Uploading.. (Takes some time)")
    time.sleep(2)
    os.system(f'{UTILS}/rclone --config={UTILS}/rclone.conf copy "{OUTPUT_PATH}" "onedrive:BUP"')
    time.sleep(2)
    os.system(f'{UTILS}/rclone --config={UTILS}/rclone.conf copy "{OUTPUT_PATH}" "mega:Uploads"')
    print("Gdrive Upload Complete!")

divider()
print("**** Weeb-DL by JoyBangla ****")
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
    os.system(f'rm -r "{TEMPORARY_PATH}" && mkdir "{TEMPORARY_PATH}" && rm -r "{OUTPUT_PATH}" && mkdir "{OUTPUT_PATH}"')
