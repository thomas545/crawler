import requests
from bs4 import BeautifulSoup
import json

playlist = "https://www.youtube.com/playlist?list=PLvFsG9gYFxY_2tiOKgs7b2lSjMwR89ECb/"
channel = "https://www.youtube.com/user/AsapSCIENCE/videos/"


def get_channel_videos(channel_url):
    data = {}
    response = requests.get(channel_url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all({"a": {'id': 'thumbnail'}}): 
        href = link.get('href')
        if 'watch' not in str(href) or 'https' in str(href):
            continue
        video_link = "https://www.youtube.com" + str(href)
        data["results"] = get_single_video(video_link)
        data['video_url'] = video_link
        for img in soup.find_all({"img": {'class': 'yt-img-shadow'}}): 
            image = img.get('data-thumb')
            data['original_full_sized'] = image
        json_data = json.dumps(data)
        return json_data

def get_single_video(url):
    result = {}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for title in soup.find_all({'h1': {'class': 'title'}}):
        result['title'] = title.string

    for view in soup.find_all({'span': {'class': 'view-count'}}):
        result['views'] = view.title
    return result


CrawlerChannel = get_channel_videos(channel)
CrawlerPlayList = get_channel_videos(playlist)
