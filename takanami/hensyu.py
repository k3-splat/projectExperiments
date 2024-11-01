import flet as ft
from flet import Text, ElevatedButton, PopupMenuItem, Row, Icon, Container, Stack, PopupMenuButton, TextField, Column, margin, colors, icons


class AppHeader(ft.Column):
    def __init__(self, file, edit, tool, display, page, on_shape_select, on_text_draw, on_freehand_draw):
        super().__init__()
        self.page = page
        self.on_shape_select = on_shape_select
        self.on_text_draw = on_text_draw
        self.on_freehand_draw = on_freehand_draw

        file_button = ElevatedButton(text="file")
        edit_button = ElevatedButton(text="edit")
        tool_button = ElevatedButton(text="tool")
        display_button = ElevatedButton(text="display")
        self.appbar_items = [
            PopupMenuItem(text="Draw Circle", on_click=lambda e: self.on_shape_select("circle")),
            PopupMenuItem(text="Draw Square", on_click=lambda e: self.on_shape_select("square")),
            PopupMenuItem(text="Draw Text", on_click=lambda e: self.on_text_draw()),
            PopupMenuItem(text="Freehand Draw", on_click=lambda e: self.on_freehand_draw())
        ]

        self.page.appbar = ft.AppBar(
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


class ShapeDrawer:
    def __init__(self, page):
        self.page = page
        self.shape_container = Stack(expand=True)
        self.current_shape = None
        self.drawing_mode = False

    def draw_shape(self, shape):
        self.current_shape = shape

        if shape == "circle":
            shape_element = ft.Draggable(
                content=Container(
                    width=100,
                    height=100,
                    bgcolor=colors.BLUE,
                    border_radius=50,
                    alignment=ft.alignment.center,
                )
            )
        elif shape == "square":
            shape_element = ft.Draggable(
                content=Container(
                    width=100,
                    height=100,
                    bgcolor=colors.RED,
                    alignment=ft.alignment.center,
                )
            )

        self.shape_container.controls.append(shape_element)
        self.page.update()

    def draw_text(self, text, x, y):
        text_element = ft.Draggable(
            content=Text(text, size=24, color=colors.BLACK),
            left=x,
            top=y,
        )
        self.shape_container.controls.append(text_element)
        self.page.update()

    def start_freehand_draw(self):
        self.drawing_mode = True

    def stop_freehand_draw(self):
        self.drawing_mode = False

    def on_mouse_move(self, e):
        if self.drawing_mode:
            # Create a small circle at the current mouse position to simulate drawing
            dot = Container(
                width=5,
                height=5,
                bgcolor=colors.BLACK,
                left=e.client_x,
                top=e.client_y,
                border_radius=2.5
            )
            self.shape_container.controls.append(dot)
            self.page.update()


def main(page: ft.Page):
    page.title = "Shape Drawer"
    page.padding = 10
    shape_drawer = ShapeDrawer(page)

    def on_shape_select(shape):
        shape_drawer.draw_shape(shape)

    def on_text_draw():
        def submit_text(e):
            text = text_input.value
            x = int(x_input.value)
            y = int(y_input.value)
            shape_drawer.draw_text(text, x, y)
            page.dialog.open = False
            page.update()

        text_input = TextField(label="Text", width=200)
        x_input = TextField(label="X Position", width=100)
        y_input = TextField(label="Y Position", width=100)
        submit_button = ElevatedButton("Draw Text", on_click=submit_text)

        popup_content = Column([text_input, x_input, y_input, submit_button], alignment="start")
        page.dialog = ft.AlertDialog(content=popup_content)
        page.dialog.open = True
        page.update()

    def on_freehand_draw():
        shape_drawer.start_freehand_draw()

    AppHeader("file", "edit", "tool", "display", page, on_shape_select, on_text_draw, on_freehand_draw)

    layout = Row(
        controls=[shape_drawer.shape_container],
        tight=False,
        expand=True,
        vertical_alignment="start",
    )

    page.add(layout)

    # Set up mouse event handlers
    page.on_mouse_move = shape_drawer.on_mouse_move
    page.on_mouse_up = lambda e: shape_drawer.stop_freehand_draw()
    
    page.update()


ft.app(target=main)
