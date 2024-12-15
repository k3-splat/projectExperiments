import flet as ft
from datetime import datetime
import time
import threading

def main(page: ft.Page):
    page.title = "タイトル画面"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

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
        on_tap=lambda e: print("見ます?")
    )

    img_kanri = ft.Image(
        src=f"/kanribotan.png",
        width=250,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    img_kanri_clickable = ft.GestureDetector(
        content=img_kanri,
        on_tap=lambda e: print("管理します?")
    )

    img_tsukuru = ft.Image(
        src=f"/tsukurubotan.png",
        width=250,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    img_tsukuru_clickable = ft.GestureDetector(
        content=img_tsukuru,
        on_tap=lambda e: print("作ります?")
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
                img_kanri_clickable,
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

ft.app(target=main, assets_dir="C:/Users/tauyo/projectExperiments/takao")