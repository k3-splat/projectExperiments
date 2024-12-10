import flet as ft
import time
import pygetwindow as gw
from PIL import ImageGrab

# mssにする

def capture_window_screenshot(window_title, output_path):
    # 指定したタイトルを持つウィンドウを取得
    windows = [w for w in gw.getAllTitles() if window_title in w]
    if not windows:
        raise Exception(f"Window with title containing '{window_title}' not found.")
    
    window = gw.getWindowsWithTitle(windows[0])[0]
    
    # ウィンドウの位置とサイズを取得
    bbox = (window.left, window.top, window.right, window.bottom)
    
    # スクリーンショットを撮る
    screenshot = ImageGrab.grab(bbox=bbox)
    screenshot.save(output_path)
    print(f"Screenshot saved to {output_path}")


def main(page: ft.Page):
    outputpath = "C:/Users/gunda/projectExperiments/Sunagawa/image/test.png"
    page.title = "Card Example"
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    )
    time.sleep(3)
    capture_window_screenshot("Card Example", outputpath)

ft.app(main)