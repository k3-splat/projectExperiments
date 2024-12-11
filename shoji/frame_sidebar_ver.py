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
import flet.canvas as cv

#AppHeader for English
class AppHeader_eng(ft.Column):
    theme_mode = "light" #Initial display theme is light

    def __init__(self, next, back, undo, display, page):
        super().__init__()
        self.page = page

        #Method of changing language English to Japanese
        def Change_Lng_Num(e):
            main(page, 1)

        #Method of changing theme
        def Theme_Change(e):
            self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
            self.page.update()

        next_button = ElevatedButton(text = "next") #Add function for file
        back_button = ElevatedButton(text = "back") #Add function for back
        undo_button = ElevatedButton(text = "undo") #Add function for undo
        display_button = ElevatedButton(text = "display") #Add function for display

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
                            #Display required buttons
                            display_button,
                            undo_button,
                            back_button,
                            next_button,
                            ft.SubmenuButton(
                                content = ft.Text("Settings"),
                                controls = [
                                    ft.SubmenuButton(
                                        content = ft.Text("Language"),
                                        controls = [
                                            ft.MenuItemButton(
                                                content = ft.Text("日本語"),
                                                on_click = Change_Lng_Num,
                                            ),
                                        ],
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

#AppHeader for Japanese
class AppHeader_jpn(ft.Column):
    def __init__(self, next, back, undo, display, page):
        super().__init__()
        self.page = page

        #Method of changing language Japanese to english
        def Change_Lng_Num(e):
            main(page, 0)

        #Method of changing theme
        def Theme_Change(e):
            self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
            self.page.update()

        next_button = ElevatedButton(text = "次へ") #Add function for file
        back_button = ElevatedButton(text = "前へ") #Add function for back
        undo_button = ElevatedButton(text = "戻す") #Add function for undo
        display_button = ElevatedButton(text = "表示") #Add function for display

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
                            #Display required buttons
                            display_button,
                            undo_button,
                            back_button,
                            next_button,
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
                                        ],
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

#Sidebar for English
class Sidebar_eng(UserControl):
    def __init__(self):
        super().__init__()
        self.nav_rail_visible = True
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
                expand = True,
                vertical_alignment = CrossAxisAlignment.START,
                visible = self.nav_rail_visible,
            )
        )
        return self.view

    def toggle_nav_rail(self, e):
        self.nav_rail.visible = not self.nav_rail.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.toggle_nav_rail_button.tooltip = "Open Side Bar" if self.toggle_nav_rail_button.selected else "Collapse Side Bar"
        self.view.update()
        self.page.update()

#Sidebar for Japanese
class Sidebar_jpn(UserControl):
    def __init__(self):
        super().__init__()
        self.nav_rail_visible = True
        self.nav_rail_items = [
            NavigationRailDestination(
                icon_content = Icon(icons.FOLDER_OUTLINED),
                selected_icon_content = Icon(icons.FOLDER_OUTLINED),
                label_content = Text("ファイル"),
            ),
            NavigationRailDestination(
                icon_content = Icon(icons.CREATE),
                selected_icon_content = Icon(icons.CREATE_OUTLINED),
                label_content = Text("編集"),
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
                expand = True,
                vertical_alignment = CrossAxisAlignment.START,
                visible = self.nav_rail_visible,
            )
        )
        return self.view

    def toggle_nav_rail(self, e):
        self.nav_rail.visible = not self.nav_rail.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.toggle_nav_rail_button.tooltip = "Open Side Bar" if self.toggle_nav_rail_button.selected else "Collapse Side Bar"
        self.view.update()
        self.page.update()

#Here is entry point -- main method
def main(page: ft.Page, ch = 0):
    chNum = ch

    def chLng(ch):
        if chNum == 0:
            page.controls.clear()
            AppHeader_eng("next", "back", "undo", "display", page)
            sidebar = Sidebar_eng()
            layout = Row(
                controls = [sidebar],
                vertical_alignment = "start",
            )
            page.add(layout)
            page.update()
        elif chNum == 1:
            page.controls.clear()
            AppHeader_jpn("next", "back", "undo", "display", page)
            sidebar = Sidebar_jpn()
            layout = Row(
                controls = [sidebar],
                vertical_alignment = "start",
            )
            page.add(layout)
            page.update()
        else:
            page.controls.clear
            AppHeader_eng("next", "back", "undo", "display", page)
            sidebar = Sidebar_eng()
            layout = Row(
                controls = [sidebar],
                vertical_alignment = "start",
            )
            page.add(layout)
            page.update()

    chLng(chNum)
    page.title = "Video Maker"
    page.padding = 10
    my_text = Text("Frame Preview Area")

ft.app(target = main)
