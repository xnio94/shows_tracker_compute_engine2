import requests
from bs4 import BeautifulSoup
import json
from munch import DefaultMunch
from datetime import datetime
import random
import m3u8
from urllib.parse import urlparse, urljoin
BASE_URL = "https://cf-st.sc-cdn.net/d/"

def get_best_resolution_stream_url(master_m3u8_url):
    response = requests.get(master_m3u8_url)
    m3u8_master = m3u8.loads(response.text)

    # Sort the playlists by resolution and get the highest one
    best_stream = sorted(m3u8_master.playlists, key=lambda x: x.stream_info.resolution[1], reverse=True)[0]
    return BASE_URL + best_stream.uri

def get_video_source_url(stream_url):
    response = requests.get(stream_url)
    m3u8_playlist = m3u8.loads(response.text)

    # Extract the video source from the m3u8 playlist
    video_source = m3u8_playlist.segments[0].uri
    return BASE_URL + video_source

def get_audio_stream_url(master_m3u8_url):
    response = requests.get(master_m3u8_url)
    m3u8_master = m3u8.loads(response.text)

    # Extract the audio stream's URI from the m3u8 playlist
    audio_stream = [media for media in m3u8_master.media if media.type == 'AUDIO'][0]
    return BASE_URL + audio_stream.uri

def get_audio_source_url(stream_url):
    response = requests.get(stream_url)
    m3u8_playlist = m3u8.loads(response.text)

    # Extract the audio source from the m3u8 playlist
    audio_source = m3u8_playlist.segments[0].uri
    return BASE_URL + audio_source

def get_video(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('script', id= '__NEXT_DATA__')
    tree = y = json.loads(s.text)
    tree = DefaultMunch.fromDict(tree)
    pageProps = tree.props.pageProps
    urls = pageProps.preselectedStory.premiumStory.playerStory.snapList
    urls = [e.snapUrls.mediaUrl for e in urls]
    urls = urls[0:-1]
    urls = [a.split('.111?')[0] for a in urls]
    episode = pageProps.preselectedStory.premiumStory.playerStory.storyTitle.value
    show = pageProps.publicProfileInfo.title
    episode_num = pageProps.preselectedStory.premiumStory.episodeNumber
    season_num = pageProps.preselectedStory.premiumStory.seasonNumber
    date = pageProps.preselectedStory.premiumStory.timestampInSec.value
    date = datetime.fromtimestamp(int(date))
    date = str(date.date())
    title = str(episode) + '_' + str(show) + '_S' + str(season_num) + '_EP' + str(episode_num) + '_' + date

    master_m3u8_url = urls[0]  #"https://cf-st.sc-cdn.net/d/Az3dP73A8VcBO2OytRmpG.1203.UHCJFQA.m3u8"
    # video
    stream_url = get_best_resolution_stream_url(master_m3u8_url)
    video_url = get_video_source_url(stream_url)
    # audio
    audio_stream = get_audio_stream_url(master_m3u8_url)
    audio_url = get_audio_source_url(audio_stream)
    return video_url, audio_url