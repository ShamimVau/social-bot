#coding=utf-8
#!/bin/python3
#############################$##############
# PYTHON SOCIAL MEDIA VIDEO DOWNLOADER BOT #
#          BOT VERSION: 1.0.0              #
#  AUTHOR : MOHAMMAD ALAMIN (anbuinfosec)  #
#      GET APIKEY : https://anbusec.xyz    #
#           COPYRIGHT : anbuinfosec        #
############################################

import os
import requests
import re
import random
import string
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def check_tmp ():
  tmp_folder = os.path.join(os.getcwd(), 'tmp')
  if not os.path.exists(tmp_folder):
    os.makedirs(tmp_folder)
    
    
def random_name():
    random_id = ''.join(random.choice(string.digits) for _ in range(10))
    return f'{random_id}.mp4'
    
def check_downloader(url):
    facebook_regex = r'(https?://)?(www\.)?(facebook\.com|fb\.watch|fb\.com|m\.facebook\.com|web\.facebook\.com)/.+$'
    youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$'
    terabox_regex = r'(https?://)?(www\.)?teraboxapp\.com/s/.+$'
    instagram_regex = r'(https?://)?(www\.)?instagram\.com/(p|reel|tv)/.+'
    twitter_regex = r'(https?://)?(www\.)?twitter\.com/.+/status/.+'
    
    if re.match(facebook_regex, url):
        return "facebook"
    elif re.match(youtube_regex, url):
        return "youtube"
    elif re.match(terabox_regex, url):
        return "terabox"
    elif re.match(instagram_regex, url):
        return "instagram"
    elif re.match(twitter_regex, url):
        return "twitter"
    else:
        return False

def downloadFromUrl(url, destination_folder='tmp'):
  response = requests.get(url)
  if response.status_code == 200:
    file_path = os.path.join(destination_folder, random_name())
    with open(file_path, "wb") as f:
      f.write(response.content)
      return file_path
  else:
    return False

def get_video_download_info(video_url, downloader):
    base_url = f'https://anbusec.xyz/api/downloader/{downloader}'
    query_params = {
        'apikey': api_key,
        'url': video_url,
        'pwd': ''
    }
    try:
        response = requests.get(base_url, params=query_params)
        response.raise_for_status()
        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        return {"status": False, "message": f"Error: {e}"}
