import flet as ft
import flet.canvas as cv
import math

class State:
    x: float
    y: float

class canVas:
    color = ft.colors.BLACK
    width = 3
    draw_mode = "free"
    
    @classmethod
    def setColor(cls, color: ft.colors):
        cls.color = color

    @classmethod
    def setWidth(cls, width: int):
        cls.width = width

    @classmethod
    def setDrawMode(cls, mode: str):
        cls.draw_mode = mode
    
    def __init__(self):
        self.state = State()
        self.current_rectangle = None
        self.current_rectangles = []
        self.current_circle = None

        self.cp = cv.Canvas(
            content=ft.GestureDetector(
                on_pan_start=self.pan_start,
                on_pan_update=self.pan_update,
                drag_interval=10,
            )
        )

    def pan_start(self, e: ft.DragStartEvent):
        self.state.x = e.local_x
        self.state.y = e.local_y

    def pan_update(self, e: ft.DragUpdateEvent):
        """ドラッグ更新時の描画処理"""
        if canVas.draw_mode == "free":  # 自由描画モード
            # 線を描画
            self.cp.shapes.append(
                cv.Line(
                    self.state.x, self.state.y, e.local_x, e.local_y,
                    paint=ft.Paint(color=canVas.color, stroke_width=canVas.width)
                )
            )
            self.cp.update()
            self.state.x = e.local_x
            self.state.y = e.local_y
        elif canVas.draw_mode == "rectangle":  # 長方形描画モード
            # 長方形を描画
            width = e.local_x - self.state.x
            height = e.local_y - self.state.y
            self.draw_rectangle(self.state.x, self.state.y, width, height)
        elif canVas.draw_mode == "circle":  # 円描画モード
            # 円を描画
            radius = max(abs(e.local_x - self.state.x), abs(e.local_y - self.state.y))
            self.draw_circle(self.state.x, self.state.y, radius)
        elif canVas.draw_mode == "Rotate":
            print("くるくる")
            self.rotate_shape()
        elif canVas.draw_mode == "Small":
            print("小さい")
            self.shrink_shapes()
        elif canVas.draw_mode == "eraser":
            print("消しゴム")
            self.erase(e)

    def erase(self, e: ft.DragUpdateEvent):
    
        eraser_color = "white" 
        self.cp.shapes.append(
            cv.Line(
                self.state.x, self.state.y, e.local_x, e.local_y,
                paint=ft.Paint(color=eraser_color, stroke_width=10)
            )   
        )
        self.cp.update()
        self.state.x = e.local_x
        self.state.y = e.local_y
    
    def shrink_shapes(self):
        #縮小
        for shape in self.cp.shapes:
            if isinstance(shape, (cv.Rect, cv.Circle, cv.Oval)):
                if isinstance(shape, cv.Rect):
                    shape.width *= 0.95 
                    shape.height *= 0.95
                elif isinstance(shape, cv.Circle):
                    shape.radius *= 0.95 
                elif isinstance(shape, cv.Oval): 
                    shape.width *= 0.95 
                    shape.height *= 0.95
                shape.update()
    
    def rotate_shape(self):
        for shape in self.cp.shapes:
            current_rotation = shape.rotate if shape.rotate is not None else 0
            shape.rotate = (current_rotation + 0.01) % 360
            shape.update() 
    
    def draw_rectangle(self, x, y, width, height):
        if self.current_rectangle is None:
            self.current_rectangle = cv.Rect(
                x=x, y=y, width=width, height=height,
                paint=ft.Paint(color=canVas.color, stroke_width=canVas.width, style="stroke")
            )
            self.store()
            self.cp.update()
        else:
            self.current_rectangle.x = x
            self.current_rectangle.y = y
            self.current_rectangle.width = width
            self.current_rectangle.height = height
            self.current_rectangle.update()
        
        self.cp.update()
    def store(self):
        self.cp.shapes.append(self.current_rectangle)
    
    def finalize_rectangle(self):
        """描画が終了した長方形を確定し、リストに追加"""
        if self.current_rectangle is not None:
            self.cp.shapes.append(self.current_rectangle)
            self.current_rectangle = None  # 描画中の長方形をリセット


    def draw_circle(self, x, y, radius):
        if self.current_circle is None:
            self.current_circle = cv.Circle(
                x=x, y=y, radius=radius,
                paint=ft.Paint(color=canVas.color, stroke_width=canVas.width, style="stroke")
            )
        # 描画中の円を `shapes` に追加
            self.cp.shapes.append(self.current_circle)
        else:
        # すでに描画中の円があれば、位置や半径を更新
            self.current_circle.x = x
            self.current_circle.y = y
            self.current_circle.radius = radius
            self.current_circle.update()

    # 描画が完了した場合、円を確定

        self.cp.update()  # 更新を呼び出して描画を反映

    def draw_oval(self, x, y, width, height):
        """楕円を描画"""
        self.cp.shapes.append(
            cv.Oval(
                x=x, y=y, width=width, height=height,
                paint=ft.Paint(color=canVas.color, stroke_width=canVas.width, style="stroke")
            )
        )
        self.cp.update()

    def makeCanvas(self):
        return ft.Container(
            self.cp,
            border_radius=0,
            width=800, # アスペクト比に準拠
            height=450
        )

    @staticmethod
    def draw_rectangle_button(page: ft.Page):
        """長方形描画モードに切り替えるボタン"""
        button = ft.TextButton(text="Rectangle Mode", on_click=lambda e: canVas.setDrawMode("rectangle"))
        page.add(button)

    @staticmethod
    def draw_circle_button(page: ft.Page):
        """円描画モードに切り替えるボタン"""
        button = ft.TextButton(text="Circle Mode", on_click=lambda e: canVas.setDrawMode("circle"))
        page.add(button)

    @staticmethod
    def free_draw_button(page: ft.Page):
        """自由描画モードに切り替えるボタン"""
        button = ft.TextButton(text="Free Draw Mode", on_click=lambda e: canVas.setDrawMode("free"))
        page.add(button)
    
def main(page: ft.Page):
    page.title = "Drawing App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # ボタンを追加
    canVas.draw_rectangle_button(page)
    canVas.draw_circle_button(page)
    canVas.free_draw_button(page)
    
    # キャンバスを作成してページに追加
    canvas = canVas()
    page.add(canvas.makeCanvas())

    page.update()

if __name__=="__main__":
    pass