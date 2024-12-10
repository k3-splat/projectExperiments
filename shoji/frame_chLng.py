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
    NavigationRail,
    NavigationRailDestination,
    NavigationRailLabelType,
    Column,
    CrossAxisAlignment,
    Image,
    GestureDetector
)

#再生ボタンに必要インポート
import time
import threading

class AppHeader_eng (ft.Column):
    theme_mode = "light"

    def __init__(self, file, edit, tool, display, page):
        super().__init__()
        self.page = page

        def Change_Lng_Num(e):
            main(page, 1)

        def Theme_Change(e):
            self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
            self.page.update()

        file_button = ElevatedButton(text = "file")
        edit_button = ElevatedButton(text = "edit")
        tool_button = ElevatedButton(text = "tool")
        display_button = ElevatedButton(text = "display")

        self.page.appbar = AppBar(
            leading = Icon(icons.TRIP_ORIGIN_ROUNDED),
            leading_width = 60,
            title = Text(value = "Project name", size = 24, text_align = "center"),
            center_title = False,
            toolbar_height = 50,
            bgcolor = colors.SURFACE_VARIANT,
            actions = [
                Container(
                    content = Row(
                        [   
                            file_button,
                            edit_button,
                            tool_button,
                            display_button,
                            ft.SubmenuButton(
                                content = ft.Text("settings"),
                                controls = [
                                    ft.SubmenuButton(
                                        content = ft.Text("Language"),
                                        controls = [
                                            ft.MenuItemButton(
                                                content = ft.Text("日本語"),
                                                on_click = Change_Lng_Num,
                                            ),
                                        ]
                                    ),
                                    ft.MenuItemButton(
                                        content = ft.Text("theme"),
                                        on_click = Theme_Change,
                                    ),
                                    ft.MenuItemButton(
                                        content = ft.Text("help"),
                                    ),
                                ],
                            ),
                        ],
                        alignment = "spaceBetween",
                    ),
                    margin = margin.only(left = 25, right = 50)
                )
            ],
        )

    def build(self):
        return self.page.appbar
 
class AppHeader_jpn (ft.Column):
    def __init__(self, file, edit, tool, display, page):
        super().__init__()
        self.page = page

        file_button = ElevatedButton(text = "ファイル")
        edit_button = ElevatedButton(text = "編集")
        tool_button = ElevatedButton(text = "ツール")
        display_button = ElevatedButton(text = "表示")

        def Change_Lng_Num(e):
            main(page,0)

        def Theme_Change(e):
            self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
            self.page.update()


        self.page.appbar = AppBar(
            leading = Icon(icons.TRIP_ORIGIN_ROUNDED),
            leading_width = 60,
            title = Text(value = "プロジェクト名", size = 24, text_align = "center"),
            center_title = False,
            toolbar_height = 50,
            bgcolor = colors.SURFACE_VARIANT,
            actions = [
                Container(
                    content = Row(
                        [
                            file_button,
                            edit_button,
                            tool_button,
                            display_button,
                            ft.SubmenuButton(
                                content = ft.Text("設定"),
                                controls = [
                                    ft.SubmenuButton(
                                        content = ft.Text("言語"),
                                        controls = [
                                            ft.MenuItemButton(
                                                content = ft.Text("English"),
                                                on_click = Change_Lng_Num,
                                            ),
                                        ]
                                    ),
                                    ft.MenuItemButton(
                                        content = ft.Text("テーマ"),
                                        on_click = Theme_Change,
                                    ),
                                    ft.MenuItemButton(
                                        content = ft.Text("ヘルプ"),
                                    ),
                                ],
                            ),

                        ],
                        alignment = "spaceBetween",
                    ),
                    margin = margin.only(left = 25, right = 50)
                )
            ],
        )

    def build(self):
        return self.page.appbar
  
def main(page: ft.Page, ch = 1):
    chNum = ch

    def chLng(ch):
        if chNum == 0:
            AppHeader_eng("file","edit", "tool", "display", page)
            page.update()
        elif chNum == 1:
            AppHeader_jpn("file","edit", "tool", "display", page)
            page.update()
        else:
            AppHeader_eng("file","edit", "tool", "display", page)
            page.update()

    chLng(chNum)
    page.title = "Video Maker"
    page.padding = 10
    my_text = Text("Frame Preview Area")
    layout = Row(
        vertical_alignment = "srart" 
    )

    page.add(layout)
    page.update()

ft.app(target = main)
