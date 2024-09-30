#!/bin/bash

# Install necessary tools
apt-get -qq install -y --no-install-recommends curl git gnupg2 unzip wget pv jq aria2 7zip

# Add Debian Buster archive key and repositories
wget -qO - https://ftp-master.debian.org/keys/archive-key-10.asc | apt-key add -
echo "deb https://mkvtoolnix.download/debian/ buster main" >> /etc/apt/sources.list.d/bunkus.org.list
echo "deb http://deb.debian.org/debian buster main contrib non-free" | tee -a /etc/apt/sources.list
apt update

# Add MKVToolNix Ubuntu Bionic repository and install mkvtoolnix
echo "deb https://mkvtoolnix.download/ubuntu/ bionic main" | tee /etc/apt/sources.list.d/mkvtoolnix.download.list
apt-get install -y mkvtoolnix

# Download and extract FFmpeg
wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz
tar xvf ffmpeg-git-amd64-static.tar.xz
cd ffmpeg-*-static && mv "${PWD}/ffmpeg" "${PWD}/ffprobe" /usr/local/bin/
cd ..

# Install rclone
curl https://rclone.org/install.sh | bash

# Download and install drivedlgo
curl -L https://github.com/jaskaranSM/drivedlgo/releases/download/1.5/drivedlgo_1.5_Linux_x86_64.gz -o drivedl.gz
7z x drivedl.gz && mv drivedlgo /usr/bin/drivedl && chmod +x /usr/bin/drivedl && rm drivedl.gz

# Download files using aria2
aria2c -x16 https://s1.indexbdh.workers.dev/0:/Youtube%20Playlist%20%20/DRMv1.7.JOY.Linux.zip
aria2c -x16 https://s1.indexbdh.workers.dev/0:/Youtube%20Playlist%20%20/JBIntro/48k1080.mkv
aria2c -x16 https://s1.indexbdh.workers.dev/0:/Youtube%20Playlist%20%20/JBIntro/48k720.mkv
aria2c -x16 https://s1.indexbdh.workers.dev/0:/Youtube%20Playlist%20%20/JBIntro/44k1080.mkv
aria2c -x16 https://s1.indexbdh.workers.dev/0:/Youtube%20Playlist%20%20/JBIntro/44k720.mkv

# Unzip downloaded files
unzip JB_intro.zip -d JBintro
unzip DRMv1.7.JOY.Linux.zip -d accounts && rm *.zip

# Make necessary files executable
chmod +x /content/accounts/DRMv1.7.AUM.Linux/utils/N_m3u8DL-RE

# Install yt-dlp from GitHub
pip3 install git+https://github.com/yt-dlp/yt-dlp

# Download rclone configuration and other files
wget https://gist.githubusercontent.com/too-noob-to-handle/6cb35d18a702a7614707af2eeef4504e/raw/rclone.conf -O /root/.config/rclone/rclone.conf
wget https://gist.githubusercontent.com/too-noob-to-handle/21f0d81a57ce0a3a163ec9d87335dbd6/raw/ZGH596AF1426AF58623AGVH.srt

# Set permissions for mp4decrypt
chmod +x /content/accounts/DRMv1.7.AUM.Linux/mp4decrypt/mp4decrypt_linux
chmod +x /content/accounts/DRMv1.7.AUM.Linux/mp4decrypt/mp4decrypt_mac

# Install lk21
python -m pip install lk21
