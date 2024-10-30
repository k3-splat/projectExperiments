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
    icons
)

class AppHeader(ft.Column):
    def __init__(self, file, edit, tool, display, page):
        super().__init__()
        self.page = page

        file_button = ElevatedButton(text = "file")
        edit_button = ElevatedButton(text = "edit")
        tool_button = ElevatedButton(text = "tool")
        display_button = ElevatedButton(text = "display")
        self.appbar_items = [
            PopupMenuItem(text = "settings"),
            PopupMenuItem(),
            PopupMenuItem(text = "help"),
        ]

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

    def build(self):
        return self.page.appbar
  
def main(page: ft.Page):
    page.title = "Video Maker"
    page.padding = 10
    my_text = Text("Frame Preview Area")
    AppHeader("file", "edit", "tool", "display", page)

    layout = Row(
        tight = False,
        expand = True,
        vertical_alignment = "start",
            )

    page.add(my_text, layout)
    page.update()

ft.app(target = main)
