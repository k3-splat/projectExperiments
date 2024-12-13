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
from canvasView import canvasClass
from dialogs import askSave
import time
import pygetwindow as gw
import subprocess
import pickle
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
                            max=8,
                            divisions=7,
                            label="{value}",
                            on_change=lambda e: canvasClass.setStrokeWidth(e.control.value)
                        )
                    ]
                )
            ]
        )


class mainView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.appheader = appHeader(self.page)
        sidebarInstance = Sidebar()
        self.sidebar = sidebarInstance.build()
        menubarInstance = menubar()
        self.menubar = menubarInstance.menubar
        width, height = canvasClass.getCanvasSize()
        self.whiteboard = ft.Container(
            padding=0,
            margin=0,
            bgcolor=ft.colors.WHITE,
            width=width,
            height=height,
            border_radius=0
        )
        self.menubar.controls.extend(
            [
                ft.TextButton(text="新しいキャンバス", on_click=lambda e: self.makeNextCanvas()),
                ft.TextButton(text="新しい背景ありキャンバス", on_click=lambda e: self.makeImageCanvas()),
                ft.TextButton(text="全消し", on_click=lambda e: self.deleteObj()),
                ft.TextButton(text="コマ消し", on_click=lambda e: self.deleteCanvas(self.currentIndex)),
                ft.TextButton(text="戻る", on_click=lambda e: self.moveCanvas(self.currentIndex - 1)),
                ft.TextButton(text="進む", on_click=lambda e: self.moveCanvas(self.currentIndex + 1)),
                ft.TextButton(text="ビデオ生成", on_click=lambda e: self.makeVideo())
            ]
        )
        self.appheader.appbar.leading = ft.IconButton(icon=ft.icons.HOME, on_click=self.savefile)

    def savefile(self, e):
        serialized_obj = []
        serialized_bg = []

        for i in range(len(self.canvases)):
            tmp_list_obj = []
            for obj in self.canvasShapesList[i]:
                if type(obj) is cv.Line:
                    tmp_list_obj.append(
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
                
            serialized_obj.append(tmp_list_obj)

            serialized_bg.append(
                {
                    "content": self.backgrounds[i].content,
                    "padding": self.backgrounds[i].padding,
                    "margin": self.backgrounds[i].margin,
                    "bgcolor": self.backgrounds[i].bgcolor,
                    "width": self.backgrounds[i].width,
                    "height": self.backgrounds[i].height,
                    "border_radius": self.backgrounds[i].border_radius
                }
            )

        with open(self.outputpath, "wb") as f:
            serialized = {"object": serialized_obj, "background": serialized_bg}
            pickle.dump(serialized, f)

        self.page.go("/startView")

    def loadfile(self):
        try:
            with open(self.outputpath, "rb") as f:
                serialized = pickle.load(f)

            serialized_obj = serialized["object"]
            serialized_bg = serialized["background"]

            for i in range(len(serialized_obj)):
                tmp_obj = []
                for obj in serialized_obj[i]:
                    if obj["type"] == "Line":
                        tmp_obj.append(
                            cv.Line(x1=obj["x1"], y1=obj["y1"], x2=obj["x2"], y2=obj["y2"], paint=ft.Paint(color=obj["color"], stroke_width=obj["stroke_width"]))
                        )

                self.loadObj.append(tmp_obj)
                self.backgrounds.append(
                    ft.Container(
                        content=serialized_bg[i]['content'],
                        padding=serialized_bg[i]['padding'],
                        margin=serialized_bg[i]['margin'],
                        bgcolor=serialized_bg[i]['bgcolor'],
                        width=serialized_bg[i]['width'],
                        height=serialized_bg[i]['height'],
                        border_radius=serialized_bg[i]['border_radius']
                    ) 
                )

        except FileNotFoundError:
            return -1

    def takeCanvasImage(self, i):
        window_title = self.page.title
        output_canvasshot = "C:/Users/gunda/projectExperiments/Sunagawa/assets/canvases"
        output_path = path.join(output_canvasshot, f"{self.projectname}_{i}.png")
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
        newCanvasInstance = canvasClass()
        self.canvasShapesList.append(newCanvasInstance.cp.shapes)
        self.currentIndex += 1
        nextCanvas = newCanvasInstance.makeCanvas()
        whiteboard = self.whiteboard
        self.canvases.insert(self.currentIndex, nextCanvas)
        self.backgrounds.append(whiteboard)
        newView = ft.View("/mainView",
            appbar=self.appheader.appbar,
            controls=[
                ft.Row(
                    controls=[
                        self.sidebar,
                        ft.Column([
                            self.menubar,
                            ft.Stack(
                                controls=[
                                    whiteboard,
                                    nextCanvas
                                ]
                            )
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
        newCanvasInstance = canvasClass()
        self.canvasShapesList.append(newCanvasInstance.cp.shapes)
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

    def deleteObj(self):
        currentCanvas = self.canvasShapesList[self.currentIndex]
        currentCanvas.clear()

    def deleteCanvas(self, pagenum):
        try:
            if len(self.canvases) == 1:
                raise IndexError

            if 0 <= pagenum <= len(self.canvases) - 1:
                del self.canvases[pagenum]
                del self.canvasShapesList[pagenum]
                del self.backgrounds[pagenum]

                if self.currentIndex >= pagenum:
                    if self.currentIndex != 0:
                        self.currentIndex -= 1

                    newView = ft.View("/mainView",
                        appbar=self.appheader.appbar,
                        controls=[
                            ft.Row(
                                controls=[
                                    self.sidebar,
                                    ft.Column([
                                        self.menubar,
                                        ft.Stack(
                                            controls=[
                                                self.backgrounds[self.currentIndex],
                                                self.canvases[self.currentIndex]
                                            ]
                                        )
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
                                    ft.Stack(
                                        controls=[
                                            self.backgrounds[pagenum],
                                            self.canvases[pagenum]
                                        ]
                                    )
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
        self.projectname = projectList.getprojectName()
        self.page.title = "プロジェクト --" + self.projectname + "--"
        self.page.padding = 10
        self.appheader.appbar.title = Text(value = self.projectname, size = 24, text_align = "center")
        binarydatas = "C:/Users/gunda/projectExperiments/Sunagawa/assets/pickles" # fletモジュール以外には明示的にパスを指定しないといけない
        self.outputpath = path.join(binarydatas, self.projectname + ".pkl")
        self.canvases = []
        self.currentIndex = 0
        self.canvasShapesList = []
        self.backgrounds = []
        self.loadObj = []

        decideResume = self.loadfile()

        if decideResume == -1:
            canvasInstancePrimary = canvasClass()
            self.canvasShapesList.append(canvasInstancePrimary.cp.shapes)
            primarycanvas = canvasInstancePrimary.makeCanvas()
            whiteboard = self.whiteboard
            self.backgrounds.append(whiteboard)
            self.canvases.append(primarycanvas)

            return ft.View("/mainView",
                appbar=self.appheader.appbar,
                controls=[
                    ft.Row(
                        controls=[
                            self.sidebar,
                            ft.Column([
                                self.menubar,
                                ft.Stack(
                                    controls=[
                                        whiteboard,
                                        primarycanvas
                                    ]
                                )
                            ], expand=False)
                        ], expand=True
                    )
                ]
            )

        else:
            for i in range(len(self.loadObj)):
                newCanvasInstance = canvasClass()
                self.canvasShapesList.append(newCanvasInstance.cp.shapes)
                newCanvasInstance.cp.shapes += self.loadObj[i]
                newCanvas = newCanvasInstance.makeCanvas()
                self.canvases.append(newCanvas)

            return ft.View("/mainView",
                appbar=self.appheader.appbar,
                controls=[
                    ft.Row(
                        controls=[
                            self.sidebar,
                            ft.Column([
                                self.menubar,
                                ft.Stack(
                                    controls=[
                                        self.backgrounds[self.currentIndex],
                                        self.canvases[self.currentIndex]
                                    ]
                                )
                            ], expand=False)
                        ],
                        expand=True
                    )
                ]
            )
        

if __name__=="__main__":
    pass