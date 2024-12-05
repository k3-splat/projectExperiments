import flet as ft
from os import path
from selectWatchVideoView import selectWatchVideo

class videoPlay:
    def __init__(self, page: ft.Page):
        self.page = page
        
    def makeView(self):
        self.page.title = "動画を見る"
        video = selectWatchVideo.getVideo()
        return ft.View("/videoPlayView", [
            ft.AppBar(
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: self.page.go("/selectWatchVideoView"), tooltip="動画選択画面に戻る"),
                title=ft.Text(path.basename(video))
            ),
            ft.Video(
                expand=True,
                playlist = [ft.VideoMedia(video)],
                playlist_mode=ft.PlaylistMode.LOOP,
                fill_color=ft.colors.BLUE_400,
                aspect_ratio=16/9,
                volume=100,
                autoplay=True,
                filter_quality=ft.FilterQuality.HIGH,
                muted=False
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)