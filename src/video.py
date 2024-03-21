from src.channel import Channel
"""Импортируем Channel для интеграции API"""
class Video:

    def __init__(self, video_id):
        """Инициализируем параметры видео"""
        self.video_id = video_id
        try:
            self.video = Channel.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
            self.video_title = self.video['items'][0]['snippet']['title']
            self.video_url = f'https://www.youtube.com/watch?v={self.video_id}'
            self.video_view_count = self.video['items'][0]['statistics']['viewCount']
            self.video_like_count = self.video['items'][0]['statistics']['likeCount']
        except:
            self.video = None
            self.video_title = None
            self.video_url = None
            self.video_view_count = None
            self.video_like_count = None

    def __str__(self):
        return self.video_title
class PLVideo(Video):
    """Наследуем параметры от Video"""
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id