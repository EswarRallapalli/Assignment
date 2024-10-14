"""Create an abstract class Media with an abstract method play().
 Then create the following subclasses:

Audio, which plays a .mp3 file.
Video, which plays a .mp4 file.
LiveStream, which plays a live stream.
Implement a function start_media(media) that takes an object of type Media and calls its play() method. 
Demonstrate polymorphism by passing different types of media to this function.

"""
from abc import ABC , abstractmethod
class Media(ABC):
    @abstractmethod
    def play(self):
        pass
class Audio(Media):
    def __init__(self,file_name):
        self.mp3file=file_name
    def play(self):
        print("Playing audio file",self.mp3file)
class Video(Media):
    def __init__(self,mp4file_name):
        self.mp4file=mp4file_name
    def play(self):
        print("Playing video file:",self.mp4file)
class LiveStream(Media):
    def __init__(self,livestream):
        self.livesteam=livestream
    def play(self):
        print("Playing LiveSteam:",self.livesteam)
def start_media(media):
        media.play()
audio=Audio("Background Music..........")
video=Video("Devara Movie")
livesteam=LiveStream("JUSTIN LIVE SHOW")
start_media(audio)
start_media(video)
start_media(livesteam)    