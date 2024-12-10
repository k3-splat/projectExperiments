import flet as ft
from datetime import datetime
import time
import threading

def main(page: ft.Page):
    page.title = "Flet example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    time_text = ft.Text(
        value="",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.ORANGE_900
    )

    def update_time():
        while True:
            current_time = datetime.now().strftime("%Y/%m/%d         %H:%M:%S")
            time_text.value = current_time
            page.update()
            time.sleep(1)

    threading.Thread(target=update_time, daemon=True).start()

    page.add(
        ft.Image(
            src="titlekamo.png",
            width=860,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        ),
        ft.Row(
            [
                ft.Container(       #時刻
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
                ft.Container(
                    content=ft.Text("見るとこ"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.ORANGE_900,
                    width=250,
                    height=200,
                    border_radius=5,
                    ink=True,
                    on_click=lambda e: print("見るよ～"),
                ),
                ft.Container(
                    content=ft.Text("ここ絵だね．"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=200,
                    height=200,
                    border_radius=5,
                ),
                ft.Container(
                    content=ft.Text("作るとこ"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.ORANGE_900,
                    width=250,
                    height=200,
                    border_radius=5,
                    ink=True,
                    on_click=lambda e: print("作るよ～"),
                ),
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
                    bgcolor=ft.colors.ORANGE_900,
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

ft.app(target=main)
