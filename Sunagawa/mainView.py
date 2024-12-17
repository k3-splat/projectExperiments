import flet as ft
from flet import(
    Text,
    TextButton,
    Row,
    AppBar,
    Icon,
    Container,
    margin,
    colors,
    icons
)
from chooseProjectView import projectList
import flet.canvas as cv
from canvasView import canvasClass
from dialogs import askSave
from dialogs import inputPageDialog
import os
import time
import pygetwindow as gw
import subprocess
import pickle
from PIL import ImageGrab
from os import path

# make header
class AppHeader_eng():
    def __init__(self, page: ft.Page):
        self.page = page

        self.appbar = AppBar(
            leading = Icon(icons.TRIP_ORIGIN_ROUNDED),
            leading_width = 60,
            title = Text(value = projectList.getprojectName(), size = 24, text_align = "center"),
            center_title = False,
            toolbar_height = 50,
            bgcolor = colors.SURFACE_VARIANT,
            actions = [
                Container(
                    content = Row(
                        [
                            ft.SubmenuButton(
                                content=ft.Text("Color"),
                                controls=[
                                    ft.MenuItemButton(
                                        content=ft.Text("White"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.WHITE),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.WHITE)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Yellow"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.YELLOW),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.YELLOW)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Light Green"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.LIGHT_GREEN),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.LIGHT_GREEN)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Green"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.GREEN),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.GREEN)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Light Blue"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.LIGHT_BLUE),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.LIGHT_BLUE)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Blue"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BLUE),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.BLUE)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Purple"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.PURPLE),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.PURPLE)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Pink"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.PINK),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.PINK)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Red"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.RED),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.RED)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Orange"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.ORANGE),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.ORANGE)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Amber"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.AMBER),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.AMBER)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Brown"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BROWN),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.BROWN)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Black"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BLACK),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.BLACK)
                                    )
                                ]
                            ),
                            ft.SubmenuButton(
                                content=ft.Text("Line's Width"),
                                controls=[
                                    ft.Slider(
                                        min=1,
                                        max=12,
                                        divisions=11,
                                        label="{value}",
                                        on_change=lambda e: canvasClass.setStrokeWidth(e.control.value)
                                    )
                                ]
                            ),
                            ft.SubmenuButton(
                                content = ft.Text("Settings"),
                                controls = [
                                    ft.SubmenuButton(
                                        content = ft.Text("Language"),
                                        controls = [
                                            ft.MenuItemButton(
                                                content = ft.Text("日本語")
                                            ),
                                        ],
                                    ),
                                    ft.MenuItemButton(
                                        content = ft.Text("Theme"),
                                        on_click = self.Theme_Change,
                                    )
                                ],
                            ),
                        ],
                        alignment = "spaceBetween",
                    ),
                    margin = margin.only(left = 25, right = 50)
                )
            ],
        )

        #Method of changing theme
    def Theme_Change(self, e):
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        self.page.update()

    def build(self):
        return self.appbar

#AppHeader for Japanese
class AppHeader_jpn():
    def __init__(self, page: ft.Page):
        self.page = page

        self.appbar = AppBar(
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
                            ft.SubmenuButton(
                                content=ft.Text("色"),
                                controls=[
                                    ft.MenuItemButton(
                                        content=ft.Text("白"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.WHITE),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.WHITE)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("黄"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.YELLOW),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.YELLOW)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("黄緑"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.LIGHT_GREEN),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.LIGHT_GREEN)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("緑"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.GREEN),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.GREEN)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("水"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.LIGHT_BLUE),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.LIGHT_BLUE)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("青"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BLUE),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.BLUE)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("紫"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.PURPLE),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.PURPLE)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("桃"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.PINK),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.PINK)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("赤"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.RED),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.RED)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("橙"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.ORANGE),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.ORANGE)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("薄橙"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.AMBER),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.AMBER)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("茶"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BROWN),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.BROWN)
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("黒"),
                                        leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BLACK),
                                        on_click=lambda e: canvasClass.setColor(ft.colors.BLACK)
                                    )
                                ]
                            ),
                            ft.SubmenuButton(
                                content=ft.Text("線の太さ"),
                                controls=[
                                    ft.Slider(
                                        min=1,
                                        max=12,
                                        divisions=11,
                                        label="{value}",
                                        on_change=lambda e: canvasClass.setStrokeWidth(e.control.value)
                                    )
                                ]
                            ),
                            ft.SubmenuButton(
                                content = ft.Text("設定"),
                                controls = [
                                    ft.SubmenuButton(
                                        content = ft.Text("言語"),
                                        controls = [
                                            ft.MenuItemButton(
                                                content = ft.Text("English")
                                            ),
                                        ],
                                    ),
                                    ft.MenuItemButton(
                                        content = ft.Text("テーマ"),
                                        on_click = self.Theme_Change,
                                    )
                                ],
                            ),
                        ],
                        alignment = "spaceBetween",
                    ),
                    margin = margin.only(left = 25, right = 50)
                )
            ],
        )

        #Method of changing theme
    def Theme_Change(self, e):
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        self.page.update()

    def build(self):
        return self.appbar


class mainView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.stackList = []
        self.fps = 1
        pick_bgimage = ft.FilePicker(on_result=self.addBgImage)
        pick_image = ft.FilePicker(on_result=self.addImage)
        self.page.overlay.extend([pick_bgimage, pick_image])
        self.inputPageNum = inputPageDialog(
            lambda e: self.copyAndclearContent(),
            lambda e: self.page.close(self.inputPageNum.inputPageDialog)
        )
        self.appheader_eng = AppHeader_eng(self.page)
        self.appheader_jpn = AppHeader_jpn(self.page)
        self.appheader_eng.appbar.actions[0].content.controls[2].controls[0].controls[0].on_click = lambda e: self.change_language_mode()
        self.appheader_jpn.appbar.actions[0].content.controls[2].controls[0].controls[0].on_click = lambda e: self.change_language_mode()
        self.appheader_eng.appbar.actions[0].content.controls.insert(
            0,
            ft.TextButton(text="Pen", on_click=lambda e: self.changeMode("free"))
        )
        self.appheader_eng.appbar.actions[0].content.controls.insert(
            1,
            ft.SubmenuButton(
                content=ft.Text("Insert"),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("Shape"),
                        controls=[
                            ft.SubmenuButton(
                                content=ft.Text("Rectangle"),
                                controls=[
                                    ft.MenuItemButton(
                                        content=ft.Text("Fill"),
                                        leading=ft.Icon(name=ft.icons.RECTANGLE),
                                        on_click=lambda e: self.changeMode("rectangle_fill")
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Stroke"),
                                        leading=ft.Icon(name=ft.icons.RECTANGLE_OUTLINED),
                                        on_click=lambda e: self.changeMode("rectangle_stroke")
                                    )
                                ]
                            ),
                            ft.SubmenuButton(
                                content=ft.Text("Circle"),
                                controls=[
                                    ft.MenuItemButton(
                                        content=ft.Text("Fill"),
                                        leading=ft.Icon(name=ft.icons.CIRCLE),
                                        on_click=lambda e: self.changeMode("circle_fill")
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("Stroke"),
                                        leading=ft.Icon(name=ft.icons.CIRCLE_OUTLINED),
                                        on_click=lambda e: self.changeMode("circle_stroke")
                                    )
                                ]
                            ),
                        ]
                    ),
                    ft.TextButton(text="Image", on_click=lambda e: pick_image.pick_files(dialog_title="Select Image", allowed_extensions=["jpg", "png"])),
                ]
            ),
        )
        self.appheader_eng.appbar.actions[0].content.controls.insert(
            4,
            ft.SubmenuButton(
                content=ft.Text("Canvas"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("New Canvas"),
                        on_click=lambda e: self.makeNextCanvas()
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Copy Canvas"),
                        on_click=lambda e: self.page.open(self.inputPageNum.inputPageDialog)
                    )
                ]
            )
        )
        self.appheader_eng.appbar.actions[0].content.controls.insert(
            5,
            ft.SubmenuButton(
                content=ft.Text("Backgrounds"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Insert Image"),
                        leading=ft.Icon(name=ft.icons.IMAGE),
                        on_click=lambda e: pick_bgimage.pick_files(dialog_title="Select Image", allowed_extensions=["jpg", "png"])
                    ),
                    ft.SubmenuButton(
                        content=ft.Text("Change Color"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("White"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.WHITE),
                                on_click=lambda e: self.changeBgcolor(ft.colors.WHITE)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Yellow"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.YELLOW),
                                on_click=lambda e: self.changeBgcolor(ft.colors.YELLOW)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Light Green"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.LIGHT_GREEN),
                                on_click=lambda e: self.changeBgcolor(ft.colors.LIGHT_GREEN)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Green"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.GREEN),
                                on_click=lambda e: self.changeBgcolor(ft.colors.GREEN)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Light Blue"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.LIGHT_BLUE),
                                on_click=lambda e: self.changeBgcolor(ft.colors.LIGHT_BLUE)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Blue"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BLUE),
                                on_click=lambda e: self.changeBgcolor(ft.colors.BLUE)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Purple"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.PURPLE),
                                on_click=lambda e: self.changeBgcolor(ft.colors.PURPLE)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Pink"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.PINK),
                                on_click=lambda e: self.changeBgcolor(ft.colors.PINK)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Red"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.RED),
                                on_click=lambda e: self.changeBgcolor(ft.colors.RED)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Orange"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.ORANGE),
                                on_click=lambda e: self.changeBgcolor(ft.colors.ORANGE)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Amber"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.AMBER),
                                on_click=lambda e: self.changeBgcolor(ft.colors.AMBER)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Brown"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BROWN),
                                on_click=lambda e: self.changeBgcolor(ft.colors.BROWN)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Black"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BLACK),
                                on_click=lambda e: self.changeBgcolor(ft.colors.BLACK)
                            )
                        ]
                    )
                ]
            )
        )
        self.appheader_eng.appbar.actions[0].content.controls.insert(
            6,
            ft.SubmenuButton(
                content=ft.Text("Manipulation"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Scaling"),
                        on_click=lambda e: self.changeMode("scaling")
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Move"),
                        on_click=lambda e: None
                    )
                ]
            )
        )
        self.appheader_eng.appbar.actions[0].content.controls.insert(
            7,
            TextButton(text="Next Canvas", on_click=lambda e: self.moveCanvas(self.currentIndex + 1))
        )
        self.appheader_eng.appbar.actions[0].content.controls.insert(
            8,
            TextButton(text="Previous Canvas", on_click=lambda e: self.moveCanvas(self.currentIndex + 1))
        )
        self.appheader_eng.appbar.actions[0].content.controls.insert(
            9,
            ft.SubmenuButton(
                content=ft.Text("Delete"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Eraser"),
                        on_click=lambda e: None
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Delete All Object"),
                        on_click=lambda e: self.deleteObj()
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Delete This Canvas"),
                        on_click=lambda e: self.deleteCanvas(self.currentIndex)
                    )
                ]
            )
        )
        self.appheader_eng.appbar.actions[0].content.controls.insert(
            10,
            TextButton(text="Generate Video", on_click=lambda e: self.makeVideo())
        )
        self.appheader_jpn.appbar.actions[0].content.controls.insert(
            0,
            ft.TextButton(text="ペン", on_click=lambda e: self.changeMode("free"))
        )
        self.appheader_jpn.appbar.actions[0].content.controls.insert(
            1,
            ft.SubmenuButton(
                content=ft.Text("挿入"),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("図形"),
                        controls=[
                            ft.SubmenuButton(
                                content=ft.Text("四角形"),
                                controls=[
                                    ft.MenuItemButton(
                                        content=ft.Text("塗りつぶし"),
                                        leading=ft.Icon(name=ft.icons.RECTANGLE),
                                        on_click=lambda e: self.changeMode("rectangle_fill")
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("空"),
                                        leading=ft.Icon(name=ft.icons.RECTANGLE_OUTLINED),
                                        on_click=lambda e: self.changeMode("rectangle_stroke")
                                    )
                                ]
                            ),
                            ft.SubmenuButton(
                                content=ft.Text("円"),
                                controls=[
                                    ft.MenuItemButton(
                                        content=ft.Text("塗りつぶし"),
                                        leading=ft.Icon(name=ft.icons.CIRCLE),
                                        on_click=lambda e: self.changeMode("circle_fill")
                                    ),
                                    ft.MenuItemButton(
                                        content=ft.Text("空"),
                                        leading=ft.Icon(name=ft.icons.CIRCLE_OUTLINED),
                                        on_click=lambda e: self.changeMode("circle_stroke")
                                    )
                                ]
                            ),
                        ]
                    ),
                    ft.TextButton(text="画像", on_click=lambda e: pick_image.pick_files(dialog_title="画像を選択", allowed_extensions=["jpg", "png"])),
                ]
            ),
        )
        self.appheader_jpn.appbar.actions[0].content.controls.insert(
            4,
            ft.SubmenuButton(
                content=ft.Text("ページ"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("新しいページ"),
                        on_click=lambda e: self.makeNextCanvas()
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("ページのコピー"),
                        on_click=lambda e: self.page.open(self.inputPageNum.inputPageDialog)
                    )
                ]
            )
        )
        self.appheader_jpn.appbar.actions[0].content.controls.insert(
            5,
            ft.SubmenuButton(
                content=ft.Text("背景"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("画像"),
                        leading=ft.Icon(name=ft.icons.IMAGE),
                        on_click=lambda e: pick_bgimage.pick_files(dialog_title="画像の選択", allowed_extensions=["jpg", "png"])
                    ),
                    ft.SubmenuButton(
                        content=ft.Text("色の変更"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("白"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.WHITE),
                                on_click=lambda e: self.changeBgcolor(ft.colors.WHITE)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("黄"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.YELLOW),
                                on_click=lambda e: self.changeBgcolor(ft.colors.YELLOW)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("黄緑"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.LIGHT_GREEN),
                                on_click=lambda e: self.changeBgcolor(ft.colors.LIGHT_GREEN)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("緑"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.GREEN),
                                on_click=lambda e: self.changeBgcolor(ft.colors.GREEN)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("水"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.LIGHT_BLUE),
                                on_click=lambda e: self.changeBgcolor(ft.colors.LIGHT_BLUE)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("青"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BLUE),
                                on_click=lambda e: self.changeBgcolor(ft.colors.BLUE)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("紫"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.PURPLE),
                                on_click=lambda e: self.changeBgcolor(ft.colors.PURPLE)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("桃"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.PINK),
                                on_click=lambda e: self.changeBgcolor(ft.colors.PINK)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("赤"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.RED),
                                on_click=lambda e: self.changeBgcolor(ft.colors.RED)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("橙"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.ORANGE),
                                on_click=lambda e: self.changeBgcolor(ft.colors.ORANGE)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("薄橙"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.AMBER),
                                on_click=lambda e: self.changeBgcolor(ft.colors.AMBER)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("茶"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BROWN),
                                on_click=lambda e: self.changeBgcolor(ft.colors.BROWN)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("黒"),
                                leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BLACK),
                                on_click=lambda e: self.changeBgcolor(ft.colors.BLACK)
                            )
                        ]
                    )
                ]
            )
        )
        self.appheader_jpn.appbar.actions[0].content.controls.insert(
            6,
            ft.SubmenuButton(
                content=ft.Text("操作"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("拡大・縮小"),
                        on_click=lambda e: self.changeMode("scaling")
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("移動"),
                        on_click=lambda e: None
                    )
                ]
            )
        )
        self.appheader_jpn.appbar.actions[0].content.controls.insert(
            7,
            TextButton(text="次のページ", on_click=lambda e: self.moveCanvas(self.currentIndex + 1))
        )
        self.appheader_jpn.appbar.actions[0].content.controls.insert(
            8,
            TextButton(text="前のページ", on_click=lambda e: self.moveCanvas(self.currentIndex - 1))
        )
        self.appheader_jpn.appbar.actions[0].content.controls.insert(
            9,
            ft.SubmenuButton(
                content=ft.Text("削除"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("消しゴム"),
                        on_click=lambda e: None
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("全消し"),
                        on_click=lambda e: self.deleteObj()
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("ページの削除"),
                        on_click=lambda e: self.deleteCanvas(self.currentIndex)
                    )
                ]
            )
        )
        self.appheader_jpn.appbar.actions[0].content.controls.insert(
            10,
            ft.SubmenuButton(
                content=ft.Text("コマの再生"),
                controls=[
                    ft.Slider(
                        min=1,
                        max=30,
                        divisions=30,
                        label="{value}fps",
                        on_change=lambda e: self.setFPS(e.control.value)
                    ),
                    ft.ElevatedButton(text="再生", on_click=lambda e: self.play())
                ]
            )
        )
        self.appheader_jpn.appbar.actions[0].content.controls.insert(
            11,
            TextButton(text="ビデオの作成", on_click=lambda e: self.makeVideo())
        )

    def copyAndclearContent(self):
        self.copyCanvas(int(self.inputPageNum.inputPageDialog.content.value))
        self.inputPageNum.inputPageDialog.content.value = ""
        self.page.close(self.inputPageNum.inputPageDialog)

    def savefile(self, e):
        serialized_stacks = []

        for stack in self.stackList:
            tmp_list_stack = []
            for layer in stack.controls:
                tmp_list_shapes = []
                if type(layer) is ft.Container:
                    if type(layer.content) is cv.Canvas:
                        for obj in layer.content.shapes:
                            if type(obj) is cv.Line:
                                tmp_list_shapes.append(
                                    {
                                        "type": "Line",
                                        "x1": obj.x1,
                                        "y1": obj.y1,
                                        "x2": obj.x2,
                                        "y2": obj.y2,
                                        "color": obj.paint.color,
                                        "stroke_width": obj.paint.stroke_width
                                    }
                                )
                            
                            elif type(obj) is cv.Rect:
                                pass

                            elif type(obj) is cv.Circle:
                                pass

                            elif type(obj) is cv.Oval:
                                pass

                            elif type(obj) is cv.Path:
                                pass

                            elif type(obj) is cv.Arc:
                                pass
                        
                        tmp_list_stack.append(tmp_list_shapes)

                    elif layer.content is None:
                        tmp_list_stack.append({
                            "type": "background",
                            "bgcolor": layer.bgcolor
                        })

                elif type(layer) is ft.Image:
                    tmp_list_stack.append({
                        "type": "background_image",
                        "src": layer.src
                    })

                elif type(layer) is ft.GestureDetector:
                    tmp_list_stack.append(
                        {
                            "type": "image",
                            "left": layer.left,
                            "top": layer.top,
                            "src": layer.content.src,
                            "width": layer.content.width,
                            "height": layer.content.height
                        }
                    )
            
            serialized_stacks.append(tmp_list_stack)

        with open(self.outputpath, "wb") as f:
            pickle.dump(serialized_stacks, f)

        self.page.go("/startView")

    def loadfile(self):
        self.stackList = []
        self.canvasInstanceList = []
        try:
            with open(self.outputpath, "rb") as f:
                serialized = pickle.load(f)

            for stack in serialized:
                tmp_list_stack = []
                for layer in stack:
                    if type(layer) is list:
                        canvas_instance = canvasClass()
                        self.canvasInstanceList.append(canvas_instance)
                        for obj in layer:
                            if obj["type"] == "Line":
                                canvas_instance.cp.shapes.append(
                                    cv.Line(x1=obj["x1"], y1=obj["y1"], x2=obj["x2"], y2=obj["y2"], paint=ft.Paint(color=obj["color"], stroke_width=obj["stroke_width"]))
                                )
                            
                            elif obj["type"] == "Rect":
                                pass

                            elif obj["type"] == "Circle":
                                pass

                            elif obj["type"] == "Oval":
                                pass

                            elif obj["type"] == "Path":
                                pass

                            elif obj["type"] == "Arc":
                                pass
                            
                        canvas = canvas_instance.makeCanvas()
                        tmp_list_stack.append(canvas)

                    elif type(layer) is dict:
                        if layer["type"] == "background":
                            width, height = canvasClass.getCanvasSize()
                            tmp_list_stack.append(
                                ft.Container(
                                    padding=0,
                                    margin=0,
                                    bgcolor=layer["bgcolor"],
                                    width=width,
                                    height=height,
                                    border_radius=0
                                )
                            )

                        elif layer["type"] == "background_image":
                            width, height = canvasClass.getCanvasSize()
                            tmp_list_stack.append(
                                ft.Image(
                                    src=layer["src"],
                                    width=width,
                                    height=height
                                )
                            )

                        elif layer["type"] == "image":
                            tmp_list_stack.append(
                                ft.GestureDetector(
                                    content=ft.Image(
                                        src=layer["src"],
                                        width=layer["width"],
                                        height=layer["height"],
                                    ),
                                    mouse_cursor=ft.MouseCursor.MOVE,
                                    drag_interval=10,
                                    on_vertical_drag_update=self.on_pan_update,
                                    left=layer["left"],
                                    top=layer["top"]
                                )
                            )
                
                tmp_stack = ft.Stack(
                    controls=tmp_list_stack
                )
                self.stackList.append(tmp_stack)

        except FileNotFoundError:
            return -1

    def takeCanvasImage(self, i):
        window_title = self.page.title
        self.output_canvasshot = "C:/Users/gunda/projectExperiments/Sunagawa/assets/canvases"
        output_path = path.join(self.output_canvasshot, f"{self.projectname}_{i}.png")
        self.refreshcanvases()
        windows = [w for w in gw.getAllTitles() if window_title in w]
        if not windows:
            raise Exception(f"Window with title containing '{window_title}' not found.")
        
        window = gw.getWindowsWithTitle(windows[0])[0]
        bbox = (window.left + 15, window.top + 88, 1030, 667)

        screenshot = ImageGrab.grab(bbox=bbox)
        screenshot.save(output_path)

    def setFPS(self, fps):
        self.fps = fps
    
    def play(self):
        for i in range(len(self.stackList)):
            time_onecanvas = 1 / self.fps
            self.moveCanvas(i)
            time.sleep(time_onecanvas)

    def makeVideo(self):
        for i in range(len(self.stackList)):
            self.moveCanvas(i)
            time.sleep(0.5)
            self.takeCanvasImage(i)

    def refreshcanvases(self):
        for _, _, canvases in os.walk(self.output_canvasshot):
            for canvas in canvases:
                if self.projectname in canvas:
                    tp = path.join(self.output_canvasshot, canvas)
                    os.remove(tp)

    def changeBgcolor(self, color):
        self.stackList[self.currentIndex].controls[0].bgcolor = color

    def addBgImage(self, e: ft.FilePickerResultEvent):
        if not e.files or len(e.files) == 0:
            return

        src = e.files.pop().path
        width, height = canvasClass.getCanvasSize()
        bgImage = ft.Image(
            src=src,
            width=width,
            height=height
        )
        self.stackList[self.currentIndex].controls.insert(1, bgImage)

    def on_pan_update(self, e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()
    
    def addImage(self, e: ft.FilePickerResultEvent):
        if not e.files or len(e.files) == 0:
            return

        src = e.files.pop().path
        image = ft.GestureDetector(
            content=ft.Image(src=src, width=100),
            mouse_cursor=ft.MouseCursor.MOVE,
            drag_interval=10,
            on_vertical_drag_update=self.on_pan_update,
            left=100,
            top=100
        )
        self.stackList[self.currentIndex].controls.append(image)

    def makeNextCanvas(self):
        newCanvasInstance = canvasClass()
        self.canvasInstanceList.append(newCanvasInstance)
        newCanvasInstance.modeChange()
        nextCanvas = newCanvasInstance.makeCanvas()
        self.currentIndex += 1
        width, height = canvasClass.getCanvasSize()
        whiteboard = ft.Container(
            padding=0,
            margin=0,
            bgcolor=ft.colors.WHITE,
            width=width,
            height=height,
            border_radius=0
        )
        newStack = ft.Stack(
            controls=[
                whiteboard,
                nextCanvas
            ]
        )
        self.stackList.insert(self.currentIndex, newStack)

        if self.language_mode == 0:
            appbar = self.appheader_jpn.appbar
        else:
            appbar = self.appheader_eng.appbar

        newView = ft.View("/mainView",
            appbar=appbar,
            controls=[
                ft.Row(
                    controls=[
                        ft.Column([
                            ft.Text(f"Page Number:{self.currentIndex}"),
                            newStack
                        ], expand=False, horizontal_alignment=ft.CrossAxisAlignment.START)
                    ],
                    expand=True
                )
            ]
        )

        self.page.views.clear()
        self.page.views.append(newView)
        self.page.update()

    def copyCanvas(self, tocopypage):
        newStack = ft.Stack()
        for layer in self.stackList[self.currentIndex].controls:
            if type(layer) is ft.Container:
                if type(layer.content) is cv.Canvas:
                    copyshapes = layer.content.shapes.copy()
                    cpCanvasInstance = canvasClass()
                    cpCanvasInstance.cp.shapes.extend(copyshapes)
                    self.canvasInstanceList.append(cpCanvasInstance)
                    cpCanvas = cpCanvasInstance.makeCanvas()
                    newStack.controls.append(cpCanvas)

                elif layer.content is None:
                    width, height = canvasClass.getCanvasSize()
                    bg = layer.bgcolor
                    newbg = ft.Container(
                        padding=0,
                        margin=0,
                        bgcolor=bg,
                        width=width,
                        height=height,
                        border_radius=0
                    )
                    newStack.controls.append(newbg)

            elif type(layer) is ft.Image:
                width, height = canvasClass.getCanvasSize()
                src = layer.src
                copyimage = ft.Image(
                    src=src,
                    width=width,
                    height=height
                )
                newStack.controls.append(copyimage)

            elif type(layer) is ft.GestureDetector:
                src = layer.content.src
                width = layer.content.width
                height = layer.content.height
                left = layer.left
                top = layer.top
                copygesture = ft.GestureDetector(
                    content=ft.Image(
                        src=src,
                        width=width,
                        height=height
                    ),
                    left=left,
                    top=top
                )
                newStack.controls.append(copygesture)

        self.stackList.insert(tocopypage, newStack)

    def deleteObj(self):
        width, height = canvasClass.getCanvasSize()
        whiteboard = ft.Container(
            padding=0,
            margin=0,
            bgcolor=ft.colors.WHITE,
            width=width,
            height=height,
            border_radius=0
        )
        self.stackList[self.currentIndex].controls.clear()
        self.stackList[self.currentIndex].controls.append(whiteboard)

        alterCanvasInstance = canvasClass()
        self.canvasInstanceList.append(alterCanvasInstance)
        alterCanvas = alterCanvasInstance.makeCanvas()
        self.stackList[self.currentIndex].controls.append(alterCanvas)

    def deleteCanvas(self, pagenum):
        try:
            if len(self.stackList) == 1:
                raise IndexError

            if 0 <= pagenum <= len(self.stackList) - 1:
                del self.stackList[pagenum]

                if self.currentIndex >= pagenum:
                    if self.currentIndex != 0:
                        self.currentIndex -= 1

                    if self.language_mode == 0:
                        newView = ft.View("/mainView",
                            appbar=self.appheader_jpn.appbar,
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Column([
                                            ft.Text(f"現在のページ:{self.currentIndex}"),
                                            self.stackList[self.currentIndex]
                                        ], expand=False, horizontal_alignment=ft.CrossAxisAlignment.START)
                                    ],
                                    expand=True
                                )
                            ]
                        )

                    else:
                        newView = ft.View("/mainView",
                            appbar=self.appheader_eng.appbar,
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Column([
                                            ft.Text(f"Page Number:{self.currentIndex}"),
                                            self.stackList[self.currentIndex]
                                        ], expand=False, horizontal_alignment=ft.CrossAxisAlignment.START)
                                    ],
                                    expand=True
                                )
                            ]
                        )


                    self.page.views.clear()
                    self.page.views.append(newView)
                    self.page.update()

            else:
                raise IndexError

        except IndexError:
            pass

    def moveCanvas(self, pagenum):
        try:
            if 0 <= pagenum <= len(self.stackList) - 1:
                self.currentIndex = pagenum
                if self.language_mode == 0:
                    newView = ft.View("/mainView", 
                        appbar=self.appheader_jpn.appbar,
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Column([
                                        ft.Text(f"現在のページ:{self.currentIndex}"),
                                        self.stackList[self.currentIndex]
                                    ], expand=False, horizontal_alignment=ft.CrossAxisAlignment.START)
                                ],
                                expand=True
                            )
                        ]
                    )

                else:
                    newView = ft.View("/mainView", 
                        appbar=self.appheader_eng.appbar,
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Column([
                                        ft.Text(f"Page Number:{self.currentIndex}"),
                                        self.stackList[self.currentIndex]
                                    ], expand=False, horizontal_alignment=ft.CrossAxisAlignment.START)
                                ],
                                expand=True
                            )
                        ]
                    )

                self.page.views.clear()
                self.page.views.append(newView)
                self.page.update()
            else:
                raise IndexError

        except IndexError:
            pass

    def changeMode(self, mode):
        canvasClass.setDrawMode(mode)

        for canvasInstance in self.canvasInstanceList:
            canvasInstance.modeChange()

    def getIntermediateFrame(self):

        self.takeCanvasImage(self.currentIndex)
        self.takeCanvasImage(self.currentIndex + 1)

        cmd = "./rife-ncnn-vulkan -0 " + "-1 1.jpg -o 01.jpg"
        subprocess.call(cmd.split())

    def change_language_mode(self):
        if self.language_mode == 0:
            self.language_mode = 1
            self.page.title = "Project --" + self.projectname + "--"
            appbar = self.appheader_eng.appbar
        else:
            self.language_mode = 0
            self.page.title = "プロジェクト --" + self.projectname + "--"
            appbar = self.appheader_jpn.appbar

        # 再描画するViewの作成
        newView = ft.View("/mainView", 
            appbar=appbar,
            controls=[
                ft.Row(
                    controls=[
                        ft.Column([
                            ft.Text(f"Page Number:{self.currentIndex}"),
                            self.stackList[self.currentIndex]
                        ], expand=False,horizontal_alignment=ft.CrossAxisAlignment.START)
                    ],
                    expand=True
                )
            ]
        )

        # ページビューの更新
        self.page.views.clear()
        self.page.clean()
        self.page.views.append(newView)
        self.page.update()


    def makeView(self):
        self.projectname = projectList.getprojectName()
        self.page.title = "プロジェクト --" + self.projectname + "--"
        self.page.padding = 10
        self.appheader_eng.appbar.title = Text(value = self.projectname, size = 24, text_align = "center")
        self.appheader_jpn.appbar.title = Text(value = self.projectname, size = 24, text_align = "center")
        binarydatas = "C:/Users/gunda/projectExperiments/Sunagawa/assets/pickles" # fletモジュール以外には明示的にパスを指定しないといけない
        self.outputpath = path.join(binarydatas, self.projectname + ".pkl")
        self.currentIndex = 0
        self.language_mode = 0

        decideResume = self.loadfile()

        if decideResume == -1:
            canvasInstancePrimary = canvasClass()
            self.canvasInstanceList.append(canvasInstancePrimary)
            primarycanvas = canvasInstancePrimary.makeCanvas()
            width, height = canvasClass.getCanvasSize()
            whiteboard = ft.Container(
                padding=0,
                margin=0,
                bgcolor=ft.colors.WHITE,
                width=width,
                height=height,
                border_radius=0
            )
            primaryStack = ft.Stack(
                controls=[
                    whiteboard,
                    primarycanvas
                ]
            )
            self.stackList.append(primaryStack)

            return ft.View("/mainView",
                appbar=self.appheader_jpn.appbar,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Column([
                                ft.Text(f"Page Number:{self.currentIndex}"),
                                primaryStack
                            ], expand=False, horizontal_alignment=ft.CrossAxisAlignment.START)
                        ], expand=True
                    )
                ]
            )

        else:
            return ft.View("/mainView",
                appbar=self.appheader_jpn.appbar,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Column([
                                ft.Text(f"Page Number:{self.currentIndex}"),
                                self.stackList[self.currentIndex]
                            ], expand=False, horizontal_alignment=ft.CrossAxisAlignment.START)
                        ],
                        expand=True
                    )
                ]
            )
        

if __name__=="__main__":
    pass