#進捗：四角形、円、自由描画、消しゴムモードの追加、next,backのボタンを使えるように
#次：テキストと変形、
#描画できる図形の数に限度あり,まだページ数は押しても意味ないです
#テスト更新できるか


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

class AppHeader:
    def __init__(self, page, draw_app):
        self.page = page
        self.draw_app = draw_app

        next_button = ElevatedButton(text="next", on_click=self.next_frame)
        back_button = ElevatedButton(text="back", on_click=self.prev_frame)
        undo_button = ElevatedButton(text="undo")
        display_button = ElevatedButton(text="display")

        self.page_number_text = Text(f"Page {self.draw_app.current_frame_index + 1}/{len(self.draw_app.frames)}")

        self.appbar_items = [
            PopupMenuItem(text="settings"),
            PopupMenuItem(),
            PopupMenuItem(text="help"),
        ]

        self.page.appbar = AppBar(
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
                            display_button,
                            undo_button,
                            back_button,
                            next_button,
                             self.page_number_text,  # ページ数
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

    def next_frame(self, e):
        self.draw_app.next_frame()

    def prev_frame(self, e):
        self.draw_app.prev_frame()

class Sidebar:
    def __init__(self):
        self.nav_rail_visible = True

        self.nav_rail_items = [
            NavigationRailDestination(
                icon_content=Icon(icons.FOLDER_OUTLINED),
                selected_icon_content=Icon(icons.FOLDER_OUTLINED),
                label_content=Text("file"),
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.CREATE),
                selected_icon_content=Icon(icons.CREATE_OUTLINED),
                label_content=Text("edit"),
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.SETTINGS),
                selected_icon_content=Icon(icons.SETTINGS_OUTLINED),
                label_content=Text("Settings"),
            ),
        ]

        self.nav_rail = NavigationRail(
            height=300,
            selected_index=None,
            label_type=NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            group_alignment=-0.9,
            destinations=self.nav_rail_items,
            on_change=lambda e: print("Selected destination: ", e.control.selected_index),
        )

        self.toggle_nav_rail_button = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT,
            icon_color=colors.BLUE_GREY_400,
            selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT,
            on_click=self.toggle_nav_rail,
            tooltip="Collapse Nav Bar",
        )

    def build(self):
        return Container(
            content=Row(
                [
                    self.nav_rail,
                    Container(
                        bgcolor=colors.BLACK26,
                        border_radius=20,
                        height=220,
                        alignment=alignment.center_right,
                        width=2
                    ),
                    self.toggle_nav_rail_button,
                ],
                expand=True,
                vertical_alignment=CrossAxisAlignment.START,
                visible=self.nav_rail_visible,
            )
        )

    def toggle_nav_rail(self, e):
        self.nav_rail.visible = not self.nav_rail.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.toggle_nav_rail_button.tooltip = "Open Side Bar" if self.toggle_nav_rail_button.selected else "Collapse Side Bar"
        self.nav_rail.update()


#ここから上がUIの部分



class DrawApp:
    def __init__(self):
        self.frames = [[]]  # フレームを管理するリスト
        self.current_frame_index = 0
        self.points = []
        self.start_x = 0 
        self.start_y = 0
        self.is_rectangle_mode = False #モード選択の時に使用
        self.is_drawing_mode = False
        self.is_circle_mode = False
        self.is_eraser_mode = False

    def build(self):
        self.draw_area = Stack([], width=500, height=400)
        self.gesture_detector = GestureDetector(
            mouse_cursor="crosshair",
            on_pan_update=self.on_pan_update,
            on_pan_start=self.on_pan_start,
            on_pan_end=self.on_pan_end,
            content=Container(
                content=self.draw_area,
                bgcolor=colors.WHITE,
                alignment=alignment.top_left
            ),
        )
        
        #ボタン
        rectangle_button = ElevatedButton(
            text="四角形",
            on_click=self.rectangle
        )

        free_draw_button = ElevatedButton(
            text="自由描画",
            on_click=self.free
        )

        circle_button = ElevatedButton(
            text="円",
            on_click=self.circle
        )

        eraser_button = ElevatedButton(
            text="消しごむ",
            on_click=self.eraser
        )

        return Column(
            controls=[
                Row(
                    controls=[rectangle_button, free_draw_button, circle_button, eraser_button],
                    alignment="center"
                ),
                self.gesture_detector
            ]
        )

    def next_frame(self):
        # 現在のフレームを保存
        self.frames[self.current_frame_index] = self.draw_area.controls.copy()
        if self.current_frame_index < len(self.frames) - 1:
            self.current_frame_index += 1
        else:
            # 新しいフレームを追加
            self.frames.append([])
            self.current_frame_index += 1
        self.load_frame()

    def prev_frame(self):
        if self.current_frame_index > 0:
            self.current_frame_index -= 1
        self.load_frame()

    def load_frame(self):
        # フレームの図形を描画エリアに表示
        self.draw_area.controls.clear()
        self.draw_area.controls.extend(self.frames[self.current_frame_index].copy())
        self.draw_area.update()

    def rectangle(self, e):
        self.is_rectangle_mode = True
        self.is_drawing_mode = False
        self.is_circle_mode = False
        self.is_eraser_mode = False

    def free(self, e):
        self.is_drawing_mode = True
        self.is_rectangle_mode = False
        self.is_circle_mode = False
        self.is_eraser_mode = False

    def circle(self, e):
        self.is_rectangle_mode = False
        self.is_drawing_mode = False
        self.is_circle_mode = True
        self.is_eraser_mode = False

    def eraser(self, e):
        self.is_rectangle_mode = False
        self.is_drawing_mode = False
        self.is_circle_mode = False
        self.is_eraser_mode = True

    def on_pan_start(self, e):
        self.start_x = e.local_x
        self.start_y = e.local_y
        self.points.clear()

    #以下、条件分岐を用いてモード選択を行う
    def on_pan_update(self, e):
        #四角形描画のところ
        if self.is_rectangle_mode:
            left = min(self.start_x, e.local_x)
            top = min(self.start_y, e.local_y)
            width = abs(e.local_x - self.start_x)
            height = abs(e.local_y - self.start_y)

            rectangle = Container(
                left=left,
                top=top,
                width=width,
                height=height,
                bgcolor=colors.BLACK,
                border_radius=0,
            )
            self.draw_area.controls.append(rectangle)

        elif self.is_drawing_mode:
            #自由描画のところ
            line = Container(
                left=self.start_x,
                top=self.start_y,
                width=2,  
                height=2, 
                bgcolor=colors.BLACK,
                border_radius=1,
            )
            self.draw_area.controls.append(line)

            self.start_x = e.local_x
            self.start_y = e.local_y

        elif self.is_circle_mode:
            #円の描画のところ
            current_radius = int(((e.local_x - self.start_x) ** 2 + (e.local_y - self.start_y) ** 2) ** 0.5)

            circle = Container(
                left=self.start_x - current_radius,
                top=self.start_y - current_radius,
                width=current_radius * 2,
                height=current_radius * 2,
                bgcolor=colors.BLACK,
                border_radius=current_radius,
            )
            self.draw_area.controls.append(circle)

        elif self.is_eraser_mode:
            #消しゴムのところ
            self.erase_shape(e.local_x, e.local_y)

        self.draw_area.update()

    def erase_shape(self, x, y):
        #消しゴムモード
        for shape in self.draw_area.controls:
            if (shape.left <= x <= shape.left + shape.width and
                shape.top <= y <= shape.top + shape.height):
                self.draw_area.controls.remove(shape)
                break

    def on_pan_end(self, e):
        pass

def main(page: ft.Page):
    page.title = "Video Maker"
    page.padding = 10

    draw_app = DrawApp()
    AppHeader(page, draw_app)
    sidebar = Sidebar()

    layout = Row(
        controls=[sidebar.build(), draw_app.build()],
        alignment="start"
    )
    
    page.add(layout)
    page.update()

ft.app(target=main)
