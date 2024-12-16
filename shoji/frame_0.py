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

    def __init__(self, file, tool, next, back, undo, display, page):
        super().__init__()
        self.page = page

        #Method of changing language English to Japanese
        def Change_Lng_Num(e):
            main(page, 1)

        #Method of changing theme
        def Theme_Change(e):
            self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
            self.page.update()

        file_button = ElevatedButton(text = "file") #Add function for file
        tool_button = ElevatedButton(text = "tool") #Add function for tool
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
                            file_button,
                            tool_button,
                            undo_button,
                            back_button,
                            next_button,
                            display_button,
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
    def __init__(self, file, tool, next, back, undo, display, page):
        super().__init__()
        self.page = page

        #Method of changing language Japanese to english
        def Change_Lng_Num(e):
            main(page, 0)

        #Method of changing theme
        def Theme_Change(e):
            self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
            self.page.update()
        
        file_button = ElevatedButton(text = "ファイル") #Add function for file
        tool_button = ElevatedButton(text = "ツール") #Add function for tool
        next_button = ElevatedButton(text = "次へ") #Add function for next
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
                            file_button,
                            tool_button,
                            undo_button,
                            back_button,
                            next_button,
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

#Here is entry point -- main method
def main(page: ft.Page, LngCh = 0):
    Lch = LngCh

    def chLng(Lch):
        if LngCh == 0:
            page.controls.clear()
            AppHeader_eng("file", "tool", "next", "back", "undo", "display", page)
            layout = Row(
                vertical_alignment = "start",
            )
            page.add(layout)
            page.update()
        elif LngCh == 1:
            page.controls.clear()
            AppHeader_jpn("file", "tool", "next", "back", "undo", "display", page)
            layout = Row(
                vertical_alignment = "start",
            )
            page.add(layout)
            page.update()
        else:
            page.controls.clear
            AppHeader_eng("file", "tool", "next", "back", "undo", "display", page)
            layout = Row(
                vertical_alignment = "start",
            )
            page.add(layout)
            page.update()

    chLng(LngCh)
    page.title = "Video Maker"
    page.padding = 10
    my_text = Text("Frame Preview Area")

ft.app(target = main)
