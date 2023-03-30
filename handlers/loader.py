from pytube import YouTube
import uuid


def download_audio(url):
    yt = YouTube(url)
    video_id = uuid.uuid4().fields[-1]
    yt.streams.filter(only_audio=True).first().download(
        "../media/audio/", f"{video_id}.mp3"
    )
    return f"../media/audio/{video_id}.mp3"
