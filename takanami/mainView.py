#テスト

#長方形の追加
#円の追加
#未だ不十分です。描画されますが、二回目描画しようとすると
#一回目に描画したものが消えます。
#縮小の追加ができた
#回転の追加まだエラーが出ます
#消しゴムの追加
#リストから削除、という風にしてもよかったですが
#自由描画のように消したいと思ったので
#背景色の自由描画と同じことをしてます
#まだ、見掛け倒しです
#消しゴムで消した後に円の縮小をするとおかしいことになります
#なぜか自由描画の縮小ができない。。
#アニメーション再生も追加
#アニメーションのページ数もどうにかしたい
#アニメーションソフトのバーの検討

#長方形？？

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


import flet as ft
import time

class mainView:
    def __init__(self, page: ft.Page):
        self.is_rectangle_mode = False
        self.start_x = 0  # ドラッグ開始位置のX座標
        self.start_y = 0  # ドラッグ開始位置のY座標
        self.selected_color = ft.colors.RED
        self.page = page
        self.appheader = appHeader(self.page)
        sidebarInstance = Sidebar()
        self.sidebar = sidebarInstance.build()
        menubarInstance = menubar()
        self.menubar = menubarInstance.menubar
        self.menubar.controls.extend(
            [
                ft.TextButton(text="新しいキャンバス", on_click=lambda e: self.makeNextCanvas()),
                ft.TextButton(text="新しい背景ありキャンバス", on_click=lambda e: self.makeImageCanvas()),
                ft.TextButton(text="戻る", on_click=lambda e: self.backCanvas()),
                ft.TextButton(text="進む", on_click=lambda e: self.goNextCanvas()),
                ft.TextButton(text="長方形", on_click=lambda e: self.switch_to_rectangle_mode()),
                ft.TextButton(text="自由描画", on_click=lambda e: self.switch_to_free_draw_mode()),
                ft.TextButton(text="円", on_click=lambda e: self.switch_to_circle_mode()),
                ft.TextButton(text="回転", on_click=lambda e: self.kurukuru()),
                ft.TextButton(text="縮小", on_click=lambda e: self.small()),
                ft.TextButton(text="消しゴム", on_click=lambda e: self.eraser()),
                ft.TextButton(text="再生", on_click=lambda e: self.playAnimation()),
                #ft.TextButton(text="コピー", on_click=lambda e: self.copyCurrentCanvas())
                #ft.TextButton(text="スピード変更", on_click=lambda e: self.changeSpeed())
            ]
        )
        self.canvases = []
        self.speed = 0.1
        self.currentIndex = 0
        self.animating = False
        self.draw_area = ft.Column()
        self.page_number_text = ft.Text(value=f"現在のページ: {self.currentIndex + 1}", size=16)


    #def copyCurrentCanvas(self):
        #print("コピー")


        #スピード調節

        self.speed_slider = ft.Slider(
            value=self.speed,
            min=0.05,
            max=1.0,
            divisions=19,
            label="{value:.2f}秒",
            on_change=self.update_speed
        )
        self.menubar.controls.append(self.speed_slider)

    def update_speed(self, e: ft.ControlEvent):
        self.speed = e.control.value
        print(f"再生スピードが {self.speed:.2f} 秒に変更されました。")

    def playAnimation(self):
        if not hasattr(self, 'animating') or not self.animating:
            self.animating = True
            self.animateFrames()
        
    def changeSpeed(self):
        if self.speed > 0.05:
            self.speed -= 0.05
        else:
            self.speed = 0.1 

        print(f"再生スピード: {self.speed}秒")

    def animateFrames(self):
        if self.canvases:
            for i in range(len(self.canvases)):
                current_canvas = self.canvases[i]
                newView = self.createView(current_canvas)
                
                self.page.views.clear()
                self.page.views.append(newView)
                self.currentIndex = len(self.canvases) - 1 
                self.page_number_text.value = f"現在のページ: {self.currentIndex + 1}"

                self.page.update()
                
                time.sleep(self.speed) 
                
                if not self.animating:
                    break 

            self.animating = False
    
    def eraser(e):
        canVas.setDrawMode("eraser")

    def small(e):
        canVas.setDrawMode("Small")
    
    def kurukuru(e):
        canVas.setDrawMode("Rotate")
    
    def switch_to_rectangle_mode(e):
        canVas.setDrawMode("rectangle")
    
    def switch_to_circle_mode(e):
        canVas.setDrawMode("circle")
    
    def switch_to_free_draw_mode(e):
        canVas.setDrawMode("free")
    
    def toggle_rectangle_mode(self):
        self.is_rectangle_mode = True
        print("長方形モード")

    def toggle_free_mode(self):
        self.is_rectangle_mode = False
        print("自由描画モード")

    def makeNextCanvas(self):
        newCanvasInstance = canVas()
        newCanvasInstance.cp.shapes.insert(0, ft.canvas.Fill(ft.Paint(ft.colors.WHITE)))
        nextCanvas = newCanvasInstance.makeCanvas()
        self.canvases.append(nextCanvas)  # インデックス管理を簡略化
        self.currentIndex = len(self.canvases) - 1  # 新しいキャンバスが最後に追加される

        newView = self.createView(nextCanvas)
        self.page.views.clear()
        self.page.views.append(newView)
        self.page_number_text.value = f"現在のページ: {self.currentIndex + 1}"
        self.page.update()


    def makeImageCanvas(self):
        newCanvasInstance = canVas()
        nextCanvas = newCanvasInstance.makeCanvas()
        imageStack = ft.Stack([  # 背景画像を含むキャンバス
            ft.Image(src="C:/Users/gunda/projectExperiments/Sunagawa/assets/titlekamo.png", width=800, height=450),
            nextCanvas
        ])
        self.canvases.append(imageStack)  # インデックス管理を簡略化
        self.currentIndex = len(self.canvases) - 1

        newView = self.createView(imageStack)
        self.page.views.clear()
        self.page.views.append(newView)
        self.page.update()

        self.page_number_text.value = f"現在のページ: {self.currentIndex + 1}"
        self.page.update()

    def backCanvas(self):
        if self.currentIndex > 0:
            self.currentIndex -= 1
            newView = self.createView(self.canvases[self.currentIndex])
            self.page.views.clear()
            self.page.views.append(newView)
            self.page.update()

            self.page_number_text.value = f"現在のページ: {self.currentIndex + 1}"
            self.page.update()

    def goNextCanvas(self):
        if self.currentIndex < len(self.canvases) - 1:  # 最後のキャンバスに到達していない場合
            self.currentIndex += 1
            newView = self.createView(self.canvases[self.currentIndex])
            self.page.views.clear()
            self.page.views.append(newView)
            self.page.update()

            self.page_number_text.value = f"現在のページ: {self.currentIndex + 1}"
            self.page.update()

    def createView(self, canvas):
        """ビューを作成するヘルパーメソッド"""
        return ft.View("/mainView",
            appbar=self.appheader.appbar,
            controls=[
                ft.Row(
                    controls=[
                        self.sidebar,
                        ft.Column([
                            self.menubar,
                            self.page_number_text,
                            canvas
                        ], expand=False)
                    ],
                    expand=True
                )
            ]
        )

    def makeView(self):
        self.page.title = "Video Maker"
        self.page.padding = 10

        self.appheader.appbar.title = ft.Text(value=projectList.getprojectName(), size=24, text_align="center")

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
    def main(page: ft.Page):
        app_view = mainView(page)
        page.views.append(app_view.makeView())
        page.update()

    ft.app(target=main)
    None