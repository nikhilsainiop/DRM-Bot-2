sudo apt update
sudo apt install ffmpeg git python3-pip
git clone https://gitHub.com/rishavdevkr/maal
cd maal 
pip3 install -r requirements.txt
python3 -m main
# NIKHIL SAINI 
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "28094744")
API_HASH  = os.environ.get("API_HASH", "a75af4285edc7747c57bb19147ca0b9b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7982396596:AAGZJZj1Gqc6XV46-9nXl-af1mhwAnLV6PU") 

#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
