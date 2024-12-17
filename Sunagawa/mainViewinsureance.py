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
from dialogs import inputPageDialog
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
        pick_bgimage = ft.FilePicker(on_result=self.addBgImage)
        pick_image = ft.FilePicker(on_result=self.addImage)
        self.page.overlay.extend([pick_bgimage, pick_image])
        self.inputPageNum = inputPageDialog(
            lambda e: self.copyAndclearContent(),
            lambda e: self.page.close(self.inputPageNum.inputPageDialog)
        )
        self.appheader = appHeader(self.page)
        sidebarInstance = Sidebar()
        self.sidebar = sidebarInstance.build()
        menubarInstance = menubar()
        self.menubar = menubarInstance.menubar
        self.menubar.controls.extend(
            [
                ft.TextButton(text="新しいキャンバス", on_click=lambda e: self.makeNextCanvas()),
                ft.TextButton(text="キャンバスのコピー", on_click=lambda e: self.page.open(self.inputPageNum.inputPageDialog)),
                ft.TextButton(text="ペン", on_click=lambda e: self.changeMode("free")),
                ft.SubmenuButton(
                    content=ft.Text("四角形"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("塗りつぶしあり"),
                            leading=ft.Icon(name=ft.icons.RECTANGLE),
                            on_click=lambda e: self.changeMode("rectangle_fill")
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("塗りつぶしなし"),
                            leading=ft.Icon(name=ft.icons.RECTANGLE_OUTLINED),
                            on_click=lambda e: self.changeMode("rectangle_stroke")
                        )
                    ]
                ),
                ft.SubmenuButton(
                    content=ft.Text("円"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("塗りつぶしあり"),
                            leading=ft.Icon(name=ft.icons.CIRCLE),
                            on_click=lambda e: self.changeMode("circle_fill")
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("塗りつぶしなし"),
                            leading=ft.Icon(name=ft.icons.CIRCLE_OUTLINED),
                            on_click=lambda e: self.changeMode("circle_stroke")
                        )
                    ]
                ),
                ft.TextButton(text="画像", on_click=lambda e: pick_image.pick_files(dialog_title="画像を選択", allowed_extensions=["jpg", "png"])),
                ft.SubmenuButton(
                    content=ft.Text("背景"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("画像の挿入"),
                            leading=ft.Icon(name=ft.icons.IMAGE),
                            on_click=lambda e: pick_bgimage.pick_files(dialog_title="画像を選択", allowed_extensions=["jpg", "png"])
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
                ),
                ft.TextButton(text="拡大・縮小", on_click=lambda e: self.changeMode("scaling")),
                ft.TextButton(text="全消し", on_click=lambda e: self.deleteObj()),
                ft.TextButton(text="コマ消し", on_click=lambda e: self.deleteCanvas(self.currentIndex)),
                ft.TextButton(text="戻る", on_click=lambda e: self.moveCanvas(self.currentIndex - 1)),
                ft.TextButton(text="進む", on_click=lambda e: self.moveCanvas(self.currentIndex + 1)),
                ft.TextButton(text="ビデオ生成", on_click=lambda e: self.makeVideo())
            ]
        )
        self.appheader.appbar.leading = ft.IconButton(icon=ft.icons.HOME, on_click=self.savefile)

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
        for i in range(len(self.stackList)):
            self.moveCanvas(i)
            time.sleep(0.5)
            self.takeCanvasImage(i)

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

        newView = ft.View("/mainView",
            appbar=self.appheader.appbar,
            controls=[
                ft.Row(
                    controls=[
                        self.sidebar,
                        ft.Column([
                            self.menubar,
                            newStack
                        ], expand=False)
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

                    newView = ft.View("/mainView",
                        appbar=self.appheader.appbar,
                        controls=[
                            ft.Row(
                                controls=[
                                    self.sidebar,
                                    ft.Column([
                                        self.menubar,
                                        self.stackList[self.currentIndex]
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
            if 0 <= pagenum <= len(self.stackList) - 1:
                self.currentIndex = pagenum
                newView = ft.View("/mainView", 
                    appbar=self.appheader.appbar,
                    controls=[
                        ft.Row(
                            controls=[
                                self.sidebar,
                                ft.Column([
                                    self.menubar,
                                    self.stackList[self.currentIndex]
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

    def changeMode(self, mode):
        canvasClass.setDrawMode(mode)

        for canvasInstance in self.canvasInstanceList:
            canvasInstance.modeChange()

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
        self.currentIndex = 0

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
                appbar=self.appheader.appbar,
                controls=[
                    ft.Row(
                        controls=[
                            self.sidebar,
                            ft.Column([
                                self.menubar,
                                primaryStack
                            ], expand=False)
                        ], expand=True
                    )
                ]
            )

        else:
            return ft.View("/mainView",
                appbar=self.appheader.appbar,
                controls=[
                    ft.Row(
                        controls=[
                            self.sidebar,
                            ft.Column([
                                self.menubar,
                                self.stackList[self.currentIndex]
                            ], expand=False)
                        ],
                        expand=True
                    )
                ]
            )
        

if __name__=="__main__":
    pass