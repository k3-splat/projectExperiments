import flet as ft
from flet import(
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
    NavigationRail,
    NavigationRailDestination,
    NavigationRailLabelType,
    Page,
    alignment,
    border_radius,
    CrossAxisAlignment,
)
from chooseProjectView import projectList
import flet.canvas as cv
from dialogs import askSave
from fileLoad import saveAndloadFile
import time
import pygetwindow as gw
import subprocess
from PIL import ImageGrab
from os import path

# make header
class appHeader:
    def __init__(self, page: Page):
        self.page = page

        # define some button
        next_button = ElevatedButton(text = "next")
        back_button = ElevatedButton(text = "back")
        undo_button = ElevatedButton(text = "undo")

        # make kebab button
        display_button = ElevatedButton(text = "display")
        self.appbar_items = [
            PopupMenuItem(text = "settings"),
            PopupMenuItem(),
            PopupMenuItem(text = "help"),
        ]

        self.appbar = AppBar(
            leading_width = 60,
            center_title = False,
            toolbar_height = 50,
            bgcolor = colors.SURFACE_VARIANT,
            actions = [
                Container(
                    content = Row(
                        [
                            display_button,
                            undo_button,
                            back_button,
                            next_button,
                            PopupMenuButton(
                                items = self.appbar_items
                            ),
                        ],
                        alignment = "spaceBetween",
                    ),
                    margin = margin.only(left = 25, right = 50)
                )
            ],
        )


class Sidebar:
    def __init__(self):
        self.nav_rail_visible = True

        # make some button
        self.nav_rail_items = [
            NavigationRailDestination(
                icon_content = Icon(icons.FOLDER_OUTLINED),
                selected_icon_content = Icon(icons.FOLDER_OUTLINED),
                label_content = Text("file"),
            ),
            NavigationRailDestination(
                icon_content = Icon(icons.CREATE),
                selected_icon_content = Icon(icons.CREATE_OUTLINED),
                label_content = Text("edit"), 
            ),
            NavigationRailDestination(
                icon_content = Icon(icons.SETTINGS),
                selected_icon_content = Icon(icons.SETTINGS_OUTLINED),
                label_content = Text("Settings"),
            ),
        ]

        self.nav_rail = NavigationRail(
            height = 300,
            selected_index = None,
            label_type=NavigationRailLabelType.ALL,
            min_width = 100,
            min_extended_width = 400,
            group_alignment = -0.9,
            destinations = self.nav_rail_items,
            on_change=lambda e: print("Selected destination: ", e.control.selected_index),
        )
        self.toggle_nav_rail_button = IconButton(
            icon = icons.ARROW_CIRCLE_LEFT,
            icon_color = colors.BLUE_GREY_400,
            selected = False,
            selected_icon = icons.ARROW_CIRCLE_RIGHT,
            on_click = self.toggle_nav_rail,
            tooltip = "Collapse Nav Bar",   
        )

    def build(self):
        self.view = Container(
            content = Row(
                [
                    self.nav_rail,
                    Container(
                        bgcolor = colors.BLACK26,
                        border_radius = border_radius.all(30),
                        height = 220,
                        alignment = alignment.center_right,
                        width = 2
                    ),
                    self.toggle_nav_rail_button,
                ],
                expand=False,
                vertical_alignment = CrossAxisAlignment.START,
                alignment=ft.MainAxisAlignment.START,
                visible = self.nav_rail_visible,
            )
        )
        return self.view

    
    def toggle_nav_rail(self, e):
        self.nav_rail.visible = not self.nav_rail.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.toggle_nav_rail_button.tooltip = "O Side Bar" if self.toggle_nav_rail_button.selected else "Collapse Side Bar"


class menubar:
    def __init__(self):
        self.menubar = ft.MenuBar(
            expand=False,
            controls=[
                ft.SubmenuButton(
                    content=ft.Text("ペンの色"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("白"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.WHITE),
                            on_click=lambda e: canVas.setColor(ft.colors.WHITE)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("黄"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.YELLOW),
                            on_click=lambda e: canVas.setColor(ft.colors.YELLOW)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("黄緑"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.LIGHT_GREEN),
                            on_click=lambda e: canVas.setColor(ft.colors.LIGHT_GREEN)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("緑"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.GREEN),
                            on_click=lambda e: canVas.setColor(ft.colors.GREEN)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("水"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.LIGHT_BLUE),
                            on_click=lambda e: canVas.setColor(ft.colors.LIGHT_BLUE)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("青"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BLUE),
                            on_click=lambda e: canVas.setColor(ft.colors.BLUE)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("紫"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.PURPLE),
                            on_click=lambda e: canVas.setColor(ft.colors.PURPLE)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("桃"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.PINK),
                            on_click=lambda e: canVas.setColor(ft.colors.PINK)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("赤"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.RED),
                            on_click=lambda e: canVas.setColor(ft.colors.RED)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("橙"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.ORANGE),
                            on_click=lambda e: canVas.setColor(ft.colors.ORANGE)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("薄橙"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.AMBER),
                            on_click=lambda e: canVas.setColor(ft.colors.AMBER)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("茶"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BROWN),
                            on_click=lambda e: canVas.setColor(ft.colors.BROWN)
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("黒"),
                            leading=ft.Icon(name=ft.icons.BRUSH, color=ft.colors.BLACK),
                            on_click=lambda e: canVas.setColor(ft.colors.BLACK)
                        )
                    ]
                ),
                ft.SubmenuButton(
                    content=ft.Text("線の太さ"),
                    controls=[
                        ft.Slider(
                            min=1,
                            max=8,
                            divisions=7,
                            label="{value}",
                            on_change=lambda e: canVas.setWidth(e.control.value)
                        )
                    ]
                )
            ]
        )


class State:
    x: float
    y: float

class canVas:
    color = ft.colors.BLACK
    stroke_width = 3
    canvasWidth = 800
    canvasHeight = 450

    @classmethod
    def setColor(cls, color: ft.colors):
        cls.color = color

    @classmethod
    def setStrokeWidth(cls, width: int):
        cls.stroke_width = width

    @classmethod
    def getCanvasSize(cls):
        return cls.canvasWidth, cls.canvasHeight

    def __init__(self):
        self.state = State()
        self.cp = cv.Canvas(
            content=ft.GestureDetector(
                on_pan_start=self.pan_start,
                on_pan_update=self.pan_update,
                drag_interval=10,
            )
        )

    def pan_start(self, e: ft.DragStartEvent):
        self.state.x = e.local_x
        self.state.y = e.local_y

    def pan_update(self, e: ft.DragUpdateEvent):
        self.cp.shapes.append(
            cv.Line(
                self.state.x, self.state.y, e.local_x, e.local_y, paint=ft.Paint(color=canVas.color, stroke_width=canVas.stroke_width)
            )
        )
        self.cp.update()
        self.state.x = e.local_x
        self.state.y = e.local_y

    def draw_rectangle(self, x, y, width, height):
        """Draws a rectangle on the canvas."""
        self.cp.shapes.append(
            cv.Rect(
                x=x, y=y, width=width, height=height,
                paint=ft.Paint(color=canVas.color, stroke_width=canVas.stroke_width, style="stroke")
            )
        )
        self.cp.update()

    def draw_circle(self, x, y, radius):
        """Draws a circle on the canvas."""
        self.cp.shapes.append(
            cv.Circle(
                x=x, y=y, radius=radius,
                paint=ft.Paint(color=canVas.color, stroke_width=canVas.stroke_width, style="stroke")
            )
        )
        self.cp.update()

    def draw_oval(self, x, y, width, height):
        """Draws an oval on the canvas."""
        self.cp.shapes.append(
            cv.Oval(
                x=x, y=y, width=width, height=height,
                paint=ft.Paint(color=canVas.color, stroke_width=canVas.stroke_width, style="stroke")
            )
        )
        self.cp.update()

    def makeCanvas(self):
        return ft.Container(
            self.cp,
            border_radius=0,
            width=800, # アスペクト比に準拠
            height=450
        )


class mainView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.appheader = appHeader(self.page)
        sidebarInstance = Sidebar()
        self.sidebar = sidebarInstance.build()
        menubarInstance = menubar()
        self.menubar = menubarInstance.menubar
        self.whiteboard = ft.canvas.Fill(ft.Paint(ft.colors.WHITE))
        self.canvases = []
        self.currentIndex = 0
        self.canvasInstanceList = []
        self.backgrounds = []
        self.menubar.controls.extend(
            [
                ft.TextButton(text="新しいキャンバス", on_click=lambda e: self.makeNextCanvas()),
                ft.TextButton(text="新しい背景ありキャンバス", on_click=lambda e: self.makeImageCanvas()),
                ft.TextButton(text="戻る", on_click=lambda e: self.moveCanvas(self.currentIndex - 1)),
                ft.TextButton(text="進む", on_click=lambda e: self.moveCanvas(self.currentIndex + 1)),
                ft.TextButton(text="ビデオ生成", on_click=lambda e: self.makeVideo())
            ]
        )
        self.appheader.appbar.title = Text(value = projectList.getprojectName(), size = 24, text_align = "center")
        self.appheader.appbar.leading = ft.IconButton(icon=ft.icons.HOME, on_click=lambda e: self.page.go("/startView"))

    def savefile(self, e):
        saving = saveAndloadFile()
        saving.savefile(projectList.getprojectName(), self.canvases)

    def takeCanvasImage(self, i):
        window_title = self.page.title
        output_canvasshot = "C:/Users/gunda/projectExperiments/Sunagawa/image"
        output_path = path.join(output_canvasshot, f"{projectList.getprojectName()}_{i}.png")
        windows = [w for w in gw.getAllTitles() if window_title in w]
        if not windows:
            raise Exception(f"Window with title containing '{window_title}' not found.")
        
        window = gw.getWindowsWithTitle(windows[0])[0]
        bbox = (window.left + 200, window.top + 170, 1600, 800)

        screenshot = ImageGrab.grab(bbox=bbox)
        screenshot.save(output_path)

    def makeVideo(self):
        for i in range(len(self.canvases)):
            self.moveCanvas(i)
            time.sleep(0.5)
            self.takeCanvasImage(i)

    def makeNextCanvas(self):
        newCanvasInstance = canVas()
        self.canvasInstanceList.append(newCanvasInstance.cp.shapes)
        self.currentIndex += 1
        newCanvasInstance.cp.shapes.insert(0, self.whiteboard)
        nextCanvas = newCanvasInstance.makeCanvas()
        self.canvases.insert(self.currentIndex, nextCanvas)
        newView = ft.View("/mainView",
            appbar=self.appheader.appbar,
            controls=[
                ft.Row(
                    controls=[
                        self.sidebar,
                        ft.Column([
                            self.menubar,
                            nextCanvas
                        ], expand=False)
                    ],
                    expand=True
                )
            ]
        )

        self.page.views.clear()
        self.page.views.append(newView)
        self.page.update()

    def makeImageCanvas(self, image=None):
        newCanvasInstance = canVas()
        self.canvasInstanceList.append(newCanvasInstance.cp.shapes)
        self.currentIndex += 1
        nextCanvas = newCanvasInstance.makeCanvas()
        background = image
        self.backgrounds.append(background)
        imageStack = ft.Stack([
            ft.Container(
                padding=0,
                margin=0,
                bgcolor=ft.colors.WHITE,
                width=800,
                height=450,
                border_radius=0
            ),
            nextCanvas
        ])
        self.canvases.insert(self.currentIndex, imageStack)
        newView = ft.View("/mainView",
            appbar=self.appheader.appbar,
            controls=[
                ft.Row(
                    controls=[
                        self.sidebar,
                        ft.Column([
                            self.menubar,
                            imageStack
                        ], expand=False)
                    ],
                    expand=True
                )
            ]
        )

        self.page.views.clear()
        self.page.views.append(newView)
        self.page.update()

    def moveCanvas(self, pagenum):
        try:
            if 0 <= pagenum <= len(self.canvases) - 1:
                self.currentIndex = pagenum
                newView = ft.View("/mainView", 
                    appbar=self.appheader.appbar,
                    controls=[
                        ft.Row(
                            controls=[
                                self.sidebar,
                                ft.Column([
                                    self.menubar,
                                    self.canvases[self.currentIndex]
                                ], expand=False)
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

    def getIntermediateFrame(self):
        self.takeCanvasImage(self.currentIndex)
        self.takeCanvasImage(self.currentIndex + 1)

        cmd = "./rife-ncnn-vulkan -0 " + "-1 1.jpg -o 01.jpg"
        subprocess.call(cmd.split())

    def makeView(self):
        self.page.title = "Video Maker"
        self.page.padding = 10

        if projectList.getprojectObj() is None:
            canvasInstancePrimary = canVas()
            canvasInstancePrimary.cp.shapes.insert(0, self.whiteboard)
            primarycanvas = canvasInstancePrimary.makeCanvas()
            self.canvases.append(primarycanvas)

            return ft.View("/mainView",
                appbar=self.appheader.appbar,
                controls=[
                    ft.Row(
                        controls=[
                            self.sidebar,
                            ft.Column([
                                self.menubar,
                                primarycanvas
                            ], expand=False)
                        ],
                        expand=True
                    )
                ]
            )

        else:
            self.canvases.extend(projectList.getprojectObj())
            return ft.View("/mainView",
                appbar=self.appheader.appbar,
                controls=[
                    ft.Row(
                        controls=[
                            self.sidebar,
                            ft.Column([
                                self.menubar,
                                self.canvases[self.currentIndex]
                            ], expand=False)
                        ],
                        expand=True
                    )
                ]
            )
        

if __name__=="__main__":
    pass