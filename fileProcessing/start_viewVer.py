import flet as ft
from datetime import datetime
import time
import threading
from dialogs import(
    chooseContiNewDialog,
    chooseWatchVideo
)

class startView:
    def __init__(self, page: ft.Page):
        self.page = page

    def update_time(self):
        while True:
            current_time = datetime.now().strftime("%Y/%m/%d         %H:%M:%S")
            self.time_text.value = current_time
            self.page.update()
            time.sleep(1)

    def startView(self):
        self.page.title = "スタート"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        choosecontinew = chooseContiNewDialog(self.page)
        choosewatchvideo = chooseWatchVideo(self.page)

        self.page.overlay.extend([choosecontinew.get_directory_dialog])

        self.time_text = ft.Text(
            value="",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.ORANGE_800
        )
        threading.Thread(target=self.update_time, daemon=True).start()

        img_title = ft.Image(
            src=f"/titlekamo.png",
            width=760,
            height=100,
            fit=ft.ImageFit.CONTAIN,
        )

        img_miru = ft.Image(
            src=f"/mirubotan.png",
            width=250,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        )

        img_miru_clickable = ft.GestureDetector(
            content=img_miru,
            on_tap=lambda e: self.page.open(choosewatchvideo.bottom_sheet),
            mouse_cursor=ft.MouseCursor.CLICK
        )

        img_tsukuru = ft.Image(
            src=f"/tsukurubotan.png",
            width=250,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        )

        img_tsukuru_clickable = ft.GestureDetector(
            content=img_tsukuru,
            on_tap=lambda e: self.page.open(choosecontinew.bottom_sheet),
            disabled=self.page.web,
            mouse_cursor=ft.MouseCursor.CLICK
        )

        return ft.View("/startView", [
            ft.Row(
                [img_title],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.Container(  # 時刻
                        content=self.time_text,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.WHITE,
                        width=400,
                        height=50,
                        border_radius=5,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    img_miru_clickable,
                    ft.Container(
                        content=ft.Text("絵"),
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.BLACK,
                        width=200,
                        height=200,
                        border_radius=5,
                    ),
                    img_tsukuru_clickable,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text("取扱説明書"),
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.ORANGE_800,
                        width=300,
                        height=50,
                        border_radius=5,
                        ink=True,
                        on_click=lambda e: self.page.go("/view2"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ], bgcolor="WHITE")

    
    def create_view2(self):
        self.page.title = "view2"

        return ft.View("/view2", [
            ft.AppBar(title=ft.Text("view2"),
                      bgcolor=ft.colors.RED),
            ft.TextField(value="view2"),
            ft.ElevatedButton(
                "Go to view1", on_click=lambda _: self.page.go("/startView")),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text("絵"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.BLACK,
                        width=200,
                        height=200,
                        border_radius=5,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ])