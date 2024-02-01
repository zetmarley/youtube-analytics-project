import json
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    """При выполнении задания homework1 os.getenv выдает ошибку"""
    """Без нее все работает исправно"""
    youtube = build('youtube', 'v3', developerKey='AIzaSyCDMMCW7ZhZcA_6SJdT2-CwocsMD4Xguu8')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        pass


    def print_info(self):
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
