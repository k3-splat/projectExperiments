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

import flet as ft
import flet.canvas as cv

class State:
    x: float
    y: float

state = State()

def main(page: ft.Page):
    page.title = "Flet Brush"

    def pan_start(e: ft.DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y

    def pan_update(e: ft.DragUpdateEvent):
        cp.shapes.append(
            cv.Line(
                state.x, state.y, e.local_x, e.local_y, paint=ft.Paint(stroke_width=3)
            )
        )
        cp.update()
        state.x = e.local_x
        state.y = e.local_y

    cp = cv.Canvas(
        [
            cv.Fill(
                ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        (0, 0), (600, 600), colors=[ft.colors.CYAN_50, ft.colors.GREY]
                    )
                )
            ),
        ],
        content=ft.GestureDetector(
            on_pan_start=pan_start,
            on_pan_update=pan_update,
            drag_interval=10,
        ),
        expand=False,
    )

    def on_pan_update1(e: ft.DragUpdateEvent):
        c.top = max(0, c.top + e.delta_y)
        c.left = max(0, c.left + e.delta_x)
        c.update()

    def on_pan_update2(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    gd = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=50,
        on_pan_update=on_pan_update1,
    )

    c = ft.Container(gd, bgcolor=ft.colors.AMBER, width=50, height=50, left=0, top=0)

    gd1 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=10,
        on_vertical_drag_update=on_pan_update2,
        left=100,
        top=100,
        content=ft.Container(bgcolor=ft.colors.BLUE, width=50, height=50),
    )

    page.add( ft.Stack([ft.Container(
            cp,
            border_radius=5,
            width=float("inf"),
            expand=True,
        ), c, gd1], width=1000, height=500))

ft.app(main)