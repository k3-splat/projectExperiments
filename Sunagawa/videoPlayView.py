import flet as ft

class videoPlay:
    def __init__(self, page: ft.Page):
        self.page = page
        self.video = ft.View("/videoPlayView", [
            ft.AppBar(
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: self.page.go("/startView"), tooltip="スタートに戻る"),
                title=ft.Text("動画タイトる")
            ),
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
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
    def makeView(self):
        self.page.title = "動画を見る"
        return self.video