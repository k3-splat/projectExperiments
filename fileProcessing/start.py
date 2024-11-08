import flet as ft
from datetime import datetime
import time
import threading
from fileLoad import (
    mkdir,
    input_material
)

class startPage:
    def __init__(self):
        ft.app(target=self.main, assets_dir="assets")

    def main(self, page: ft.Page):
        page.title = "スタート"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.bgcolor = ft.colors.WHITE

        make_directory = mkdir(page)
        get_directory_dialog = ft.FilePicker(on_result=make_directory.get_directory_path)

        mkdir.mkdir_dlg.actions[0].on_click = make_directory.make_directory
        mkdir.mkdir_dlg.actions[1].on_click = lambda e: page.close(mkdir.mkdir_dlg)

        pick_material = input_material()
        pick_material_dialog = ft.FilePicker(on_result=pick_material.pick_files_result)

        time_text = ft.Text(
            value="",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.ORANGE_800
        )

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
            on_tap=lambda e: print("見たな?"),
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
            on_tap=lambda e: print("まだ作れませ～ん"),
            mouse_cursor=ft.MouseCursor.CLICK
        )

        def update_time():
            while True:
                current_time = datetime.now().strftime("%Y/%m/%d         %H:%M:%S")
                time_text.value = current_time
                page.update()
                time.sleep(1)

        threading.Thread(target=update_time, daemon=True).start()

        page.add(
            ft.Row(
                [img_title],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.Container(  # 時刻
                        content=time_text,
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
                        margin=10,
                        padding=10,
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
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.ORANGE_800,
                        width=300,
                        height=50,
                        border_radius=5,
                        ink=True,
                        on_click=lambda e: print("説明します．"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )