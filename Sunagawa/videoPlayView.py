import flet as ft

class videoPlay:
    def __init__(self):
        self.video = ft.View("/videoPlay", [
            ft.Video(
                expand=True,
                playlist = [ft.VideoMedia("C:/Users/gunda/projectExperiments/Sunagawa/assets/Flopping.mp4")],
                playlist_mode=ft.PlaylistMode.LOOP,
                fill_color=ft.colors.BLUE_400,
                aspect_ratio=16/9,
                volume=100,
                autoplay=False,
                filter_quality=ft.FilterQuality.HIGH,
                muted=False
            ),
        ])
        
    def makeView(self):
        return self.video