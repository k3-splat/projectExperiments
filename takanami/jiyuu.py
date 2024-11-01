#自由描画


import flet as ft
from flet import (
    Text,
    ElevatedButton,
    PopupMenuItem,
    Row,
    IconButton,
    AppBar,
    Icon,
    Container,
    PopupMenuButton,
    margin,
    colors,
    icons,
    GestureDetector,
    alignment,
    Stack,
)

class AppHeader(ft.Column):
    def __init__(self, file, edit, tool, display, page):
        super().__init__()
        self.page = page

        file_button = ElevatedButton(text="file")
        edit_button = ElevatedButton(text="edit")
        tool_button = ElevatedButton(text="tool")
        display_button = ElevatedButton(text="display")
        self.appbar_items = [
            PopupMenuItem(text="settings"),
            PopupMenuItem(),
            PopupMenuItem(text="help"),
        ]

        self.page.appbar = AppBar(
            leading=Icon(icons.TRIP_ORIGIN_ROUNDED),
            leading_width=60,
            title=Text(value="Project name", size=24, text_align="center"),
            center_title=False,
            toolbar_height=50,
            bgcolor=colors.SURFACE_VARIANT,
            actions=[
                Container(
                    content=Row(
                        [
                            file_button,
                            edit_button,
                            tool_button,
                            display_button,
                            PopupMenuButton(
                                items=self.appbar_items
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    margin=margin.only(left=25, right=50)
                )
            ],
        )

    def build(self):
        return self.page.appbar

class DrawApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.points = []

    def build(self):
        self.draw_area = Container(
            content=Stack([]),
            width=500,
            height=400,
            bgcolor=colors.WHITE,
            alignment=alignment.top_left
        )

        self.gesture_detector = GestureDetector(
            mouse_cursor="crosshair",
            on_pan_update=self.on_pan_update,
            on_pan_start=self.on_pan_start,
            on_pan_end=self.on_pan_end,
            content=self.draw_area
        )
        return self.gesture_detector

    def on_pan_start(self, e):
        self.points.clear()

    def on_pan_update(self, e):
        point = Container(
            width=4,
            height=4,
            bgcolor=colors.BLACK,
            left=e.local_x,
            top=e.local_y,
            border_radius=2,
        )
        self.draw_area.content.controls.append(point)
        self.update()

    def on_pan_end(self, e):
        pass

def main(page: ft.Page):
    page.title = "Video Maker"
    page.padding = 10

    AppHeader("file", "edit", "tool", "display", page)

    # 描画エリアを生成
    draw_app = DrawApp()

    layout = Row(
        controls=[draw_app],
        tight=False,
        expand=True,
        vertical_alignment="start",
    )

    page.add(layout)
    page.update()

ft.app(target=main)
