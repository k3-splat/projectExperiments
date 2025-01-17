#進捗：四角形、円、自由描画、消しゴムモードの追加、next,backのボタンを使えるように
#次：テキストと変形、
#描画できる図形の数に限度あり,まだページ数は押しても意味ないです
#テスト更新できるか
#再生ボタン追加play
#各ページの保存があまりできてません。一度playボタンをおすとなぜか保存されます。
#拡大縮小はまだエラーが出るので、修正中です。

#11/27 
#再生速度変更できるようにしました。
#拡大縮小、回転はエラーが出ないようになりましたが、思ってたのとは違う動きになります。
#色変更ができるようになりました。細かい色変更も実装したいです。
#画像を挿入できるようにしたい

#12/4
#画像挿入をしようとしましたが、エラーになってしまいます。
#致命的なバグあり、ある程度描画すると描画できなくなります。
#↑リソースの問題？？
#回転ができるようになりました。しかし、まだ改良の余地あり...

#12/11
#mainView.pyやcanvasView.pyを参考にしています。
#このプログラムにCanvasをうまく入れることができず
#現在難航しております。
#とりあえず滑らかな自由描画はできるようにしたいです。
#canvas cvはなんとか
#cpが、うまくいかないです。
#仮にうまくいった場合、すべてcpに差し替えます。
#ページ数を実装しました。
#asyncio を使用しました。

#flet最新版だと色が使えない？
#flet 0.24.00で動作確認済み
#0.25.0では動きませんでした。
#

#やりたいことリスト
#×音声をつける
#▲変形（回転、拡大縮小）
#×範囲選択　（範囲を指定し、移動などができる。）
#×透かし　（前のコマのイラストをすかす）
#〇図形　（三角形、四角形、円などを描画する）
#×コピー　貼り付け　（現在のコマを、ほかのコマにコピーする）
#×画像の取り込み
#〇コマの速度の変更
#〇再生、停止
#〇色変更
#×テキストの表示
#自由描画の太さを変える


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
    GestureDetector,
    Slider,
    Dropdown,
    dropdown,
    Page,
)

#再生ボタンに必要インポート
import time
import threading


class AppHeader:
    def __init__(self, page, draw_app):
        self.page = page
        self.draw_app = draw_app

        next_button = ElevatedButton(text="next", on_click=self.next_frame)
        back_button = ElevatedButton(text="back", on_click=self.prev_frame)
        undo_button = ElevatedButton(text="undo")
        display_button = ElevatedButton(text="display")
        play_button = ElevatedButton(text="play,",  on_click=self.play_animation)
        
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
                            play_button,  # 再生ボタン
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

    def play_animation(self, e):
        self.draw_app.play_animation()

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
import asyncio

class DrawApp:
    def __init__(self):
        self.frames = [[]]  # フレームを管理するリスト
        self.current_frame_index = 0
        self.is_playing = False  # 再生中かどうか
        self.play_thread = None  
        self.points = []
        self.start_x = 0 
        self.start_y = 0
        self.is_rectangle_mode = False #モード選択の時に使用
        self.is_drawing_mode = False
        self.is_circle_mode = False
        self.is_eraser_mode = False
        self.zenksi_mode = False
        self.is_rotate_mode = False
        self.is_scale_mode = False 
        self.image_mode = False #ガゾウモード
        #self.page = page  

        self.selected_color = colors.BLACK
        self.pen_thickness = 5

        self.rotate = 0
        self.play_speed = 0.5
        self.page_label = Text(f"Page: {self.current_frame_index + 1}")
        self.play_task = None

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
        
        self.play_speed_slider = Slider(
            min=0.1,
            max=2.0,
            value=self.play_speed,
            divisions=19,
            label=f"Speed: {self.play_speed:.1f} sec/frame",
            on_change=self.change_play_speed,
        )

        speed_label = Text(f"Speed: {self.play_speed:.1f} sec/frame")

        #色を変える
        color_picker = Dropdown(
            label="色を選択",
            options=[
                dropdown.Option(colors.RED, "赤"),
                dropdown.Option(colors.GREEN, "緑"),
                dropdown.Option(colors.BLUE, "青"),
                dropdown.Option(colors.YELLOW, "黄"),
                dropdown.Option(colors.BLACK, "黒"),
                #dropdown.Option(colors.PURPLE, "紫"),
            ],
            value=self.selected_color,
            on_change=self.change_color,
        )

        #ボタン
        rectangle_button = ElevatedButton(
            text="Rectangle",
            on_click=self.rectangle
        )

        free_draw_button = ElevatedButton(
            text="freeDraw",
            on_click=self.free
        )

        circle_button = ElevatedButton(
            text="circle",
            on_click=self.circle
        )

        eraser_button = ElevatedButton(
            text="eraser",
            on_click=self.eraser
        )

        rotate_button = ElevatedButton(
            text="rotate",
            on_click=self.rotate_mode
        )

        scale_button = ElevatedButton(
            text="small", 
            on_click=self.scale_mode
        )

        #全部消す
        zenkesi_button = ElevatedButton(
            text="delite",
            on_click=self.zenkesi
        )

        return Column(
            controls=[
                Row(
                    controls=[rectangle_button, free_draw_button, circle_button, eraser_button, rotate_button, scale_button, zenkesi_button, color_picker],
                    alignment="center"
                ),
                speed_label,
                self.play_speed_slider,
                self.page_label,
                self.gesture_detector
            ]
        )

    def change_color(self, e):
        self.selected_color = e.control.value
        self.draw_area.update()

    
    def insert_image(self, e):
        # ファイル選択ダイアログを開く
        self.page.dialog = ft.FilePicker(
            on_result=self.on_image_selected
        )
        self.page.dialog.pick_files(allowed_extensions=["png", "jpg", "jpeg"])
    
    def on_image_selected(self, e):
        if e.files:
            selected_image = e.files[0].path
            image_container = Container(
                content=Image(
                    src=selected_image,
                    fit="contain", 
                    width=200,
                    height=200,
                ),
                left=100,
                top=100
            )
            self.draw_area.controls.append(image_container)
            self.draw_area.update()
            self.frames[self.current_frame_index].append(image_container)

    def start_play_animation(self):
        loop = asyncio.new_event_loop()
        threading.Thread(target=self.run_play, args=(loop,)).start()

    def run_play(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.play_animation())
    
    #再生するところ
    async def play_animation(self):
        if self.is_playing:
            self.is_playing = False
            if self.play_task:
                self.play_task.cancel()
            return

        self.is_playing = True

        async def play():
            while self.is_playing:
                self.next_frame()
                await asyncio.sleep(self.play_speed)
                #time.sleep(self.play_speed)

                if self.current_frame_index == len(self.frames) - 1:
                    self.is_playing = False 
                
                if self.current_frame_index == len(self.frames):
                    self.current_frame_index = 0
                    self.load_frame()
        
        #self.play_task = asyncio.create_task(play())
        await play()
        #self.play_thread = threading.Thread(target=play)
        #self.play_thread.start()

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

        self.page_label.value = f"Page: {self.current_frame_index + 1}"
        self.page_label.update()
        
#asyncio

    #スピードを変える
    def change_play_speed(self, e):
        self.play_speed = e.control.value 
        self.play_speed_slider.label = f"Speed: {self.play_speed:.1f} sec/frame" 
        self.play_speed_slider.update()
    
    def rectangle(self, e):
        self.is_rotate_mode = False
        self.is_scale_mode = False
        self.is_rectangle_mode = True
        self.is_drawing_mode = False
        self.is_circle_mode = False
        self.is_eraser_mode = False
        self.zenkesi = False

    def free(self, e):
        self.is_rotate_mode = False
        self.is_scale_mode = False
        self.is_drawing_mode = True
        self.is_rectangle_mode = False
        self.is_circle_mode = False
        self.is_eraser_mode = False
        self.zenkesi = False

    def circle(self, e):
        self.is_rotate_mode = False
        self.is_scale_mode = False
        self.is_rectangle_mode = False
        self.is_drawing_mode = False
        self.is_circle_mode = True
        self.is_eraser_mode = False
        self.zenkesi = False

    def eraser(self, e):
        self.is_rotate_mode = False
        self.is_scale_mode = False
        self.is_rectangle_mode = False
        self.is_drawing_mode = False
        self.is_circle_mode = False
        self.is_eraser_mode = True
        self.zenkesi = False
    
    def zenkesi(self, e):
        self.is_rotate_mode = False
        self.is_scale_mode = False
        self.is_rectangle_mode = False
        self.is_drawing_mode = False
        self.is_circle_mode = False
        self.is_eraser_mode = False
        self.zenkesi = True

    def rotate_mode(self, e):
        self.is_rotate_mode = True
        self.is_scale_mode = False
        self.is_rectangle_mode = False
        self.is_drawing_mode = False
        self.is_circle_mode = False
        self.is_eraser_mode = False
        self.zenkesi = False

    def scale_mode(self, e):
        self.is_rotate_mode = False
        self.is_scale_mode = True
        self.is_rectangle_mode = False
        self.is_drawing_mode = False
        self.is_circle_mode = False
        self.is_eraser_mode = False
        self.zenkesi = False

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
                bgcolor=self.selected_color,
                border_radius=0,
            )
            self.draw_area.controls.append(rectangle)

        elif self.is_drawing_mode:
            #自由描画のところ
            line = Container(
                left=self.start_x,
                top=self.start_y,
                width=5,
                height=5, 
                bgcolor=self.selected_color,
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
                bgcolor=self.selected_color,
                border_radius=current_radius,
            )
            self.draw_area.controls.append(circle)

        elif self.is_eraser_mode:
            #消しゴムのところ
            self.erase_shape(e.local_x, e.local_y)

        elif self.zenkesi:
            self.clear_all()
            self.draw_area.controls.clear()
            self.draw_area.update()

        elif self.is_rotate_mode:
            for shape in self.draw_area.controls:
                current_rotation = shape.rotate if shape.rotate is not None else 0
                shape.rotate = (current_rotation + 0.01) % 360
                shape.update()
        elif self.is_scale_mode:
            for shape in self.draw_area.controls:
                shape.width *= 0.9
                shape.height *= 0.9
        self.draw_area.update()

    def clear_all(self):
    #全ての図形を消去
        self.draw_area.controls.clear()
        self.draw_area.update()


    def erase_shape(self, x, y):
        #消しゴムモード
        for shape in self.draw_area.controls:
            if (shape.left <= x <= shape.left + shape.width and
                shape.top <= y <= shape.top + shape.height):
                self.draw_area.controls.remove(shape)
                break
    
    def zenkesi(self, x, y):
        self.draw_area.controls.clear() 
        self.draw_area.update()


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