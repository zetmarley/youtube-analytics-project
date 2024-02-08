import json
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    """При выполнении задания homework1 os.getenv выдает ошибку"""
    """Без нее все работает исправно"""
    youtube = build('youtube', 'v3', developerKey='AIzaSyCDMMCW7ZhZcA_6SJdT2-CwocsMD4Xguu8')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        """Выводит название и ссылку канала"""
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """Выводит сумму подписчиков"""
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        """Выводит разноость подписчиков"""
        result = abs(int(self.subscriber_count) - int(other.subscriber_count))
        return result

    def __it__(self, other):
        """Сравнение меньше"""
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """Сравнение меньше или равно"""
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        """Сравнение больше"""
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """Сравнение больше или равно"""
        return self.subscriber_count >= other.subscriber_count

    def __eq__(self, other):
        """Сравнение равно"""
        return self.subscriber_count == other.subscriber_count

    @property
    def channel_id(self):
        """Геттер id канала"""
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Возвращаем объект для работы с YouTube API"""
        return cls.youtube

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        """Создаем файл с данными по каналу"""
        with open(f'../saves/{file_name}.json', 'w') as f:
            mydict = {"channel_id" : self.channel_id,
            "title" : self.title,
            "description" : self.description,
            "utl" : self.url,
            "subscriber_count" : self.subscriber_count,
            "video_count" : self.video_count}
            json.dump(mydict, f)