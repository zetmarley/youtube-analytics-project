from src.channel import Channel
import isodate
from datetime import datetime, timedelta
"""Импортируем нужные библиотеки"""

class PlayList:
    def __init__(self, playlist_id):
        """Инициализируем данные плейлиста"""
        self.playlist_id = playlist_id
        self.playlist = Channel.youtube.playlistItems().list(playlistId=self.playlist_id, part=['contentDetails', 'snippet'], maxResults=50).execute()
        self.playlists = Channel.youtube.playlists().list(channelId=self.playlist['items'][0]['snippet']['channelId'], part='contentDetails,snippet', maxResults=50).execute()
        self.playlist_url = f'https://www.youtube.com/playlist?list={self.playlist_id}'
        self.playlist_videos = Channel.youtube.playlistItems().list(playlistId=self.playlist_id, part='contentDetails', maxResults=50).execute()
        self.video_ids = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = Channel.youtube.videos().list(part='contentDetails,statistics', id=','.join(self.video_ids)).execute()
        for i in self.playlists['items']:
            if self.playlist['items'][0]['snippet']['resourceId']['videoId'] in i['snippet']['thumbnails']['default']['url']:
                self.playlist_title = i['snippet']['title']

    @property
    def total_duration(self):
        """Метод выводит общую продолжительность плейлиста"""
        tm = timedelta(hours=0, minutes=0, seconds=0)
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            tm += duration
        return tm

    def show_best_video(self):
        """Метод выводит ссылку на самую залайканнрое видео"""
        mydict= {}
        result = 'https://youtu.be/'
        for i in self.video_ids:
            mydict[i] = int(Channel.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=i).execute()['items'][0]['statistics']['likeCount'])
        for k, v in mydict.items():
            if v == max(mydict.values()):
                result += k
        return result



