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
    FloatingActionButton,
    UserControl,
    CrossAxisAlignment,
)
from chooseProjectView import projectList
from canvasView import canVas

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
            leading = IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: self.page.go("/startView"), tooltip="スタートへ戻る"),
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
                ft.TextButton(text="戻る", on_click=lambda e: self.backCanvas()),
                ft.TextButton(text="進む", on_click=lambda e: self.goNextCanvas())
            ]
        )
        self.canvases = []
        self.currentIndex = 0

    def makeNextCanvas(self):
        newCanvasInstance = canVas()
        self.currentIndex += 1
        newCanvasInstance.cp.shapes.insert(self.currentIndex, ft.canvas.Fill(ft.Paint(ft.colors.WHITE)))
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

    def makeImageCanvas(self):
        newCanvasInstance = canVas()
        self.currentIndex += 1
        nextCanvas = newCanvasInstance.makeCanvas()
        imageStack = ft.Stack([
            ft.Image(
                src="C:/Users/gunda/projectExperiments/Sunagawa/assets/titlekamo.png",
                width=800,
                height=450
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

    def backCanvas(self):
        if self.currentIndex > 0:
            self.currentIndex -= 1
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

    def goNextCanvas(self):
        if self.currentIndex < len(self.canvases):
            self.currentIndex += 1
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

    def makeView(self):
        self.page.title = "Video Maker"
        self.page.padding = 10

        self.appheader.appbar.title = Text(value = projectList.getprojectName(), size = 24, text_align = "center")

        canvasInstancePrimary = canVas()
        canvasInstancePrimary.cp.shapes.insert(0, ft.canvas.Fill(ft.Paint(ft.colors.WHITE)))
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

if __name__=="__main__":
    None