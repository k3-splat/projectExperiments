import flet as ft
import cv2
from pathDatabase import pathDatabase

class selectWatchVideo:
    def __init__(self):
        self.refresh_video()

    def refresh_video(self):
        db = pathDatabase()
        self.videos = db.get_video()
        print(self.videos)

if __name__=="__main__":
    video = selectWatchVideo()        