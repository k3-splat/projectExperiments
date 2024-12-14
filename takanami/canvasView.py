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
        #self.is_dragging = None
        self.shapes = []
        #辞書
        shapes = [
                    {"type": "rect", "x": 50, "y": 50, "width": 100, "height": 50, "rotation_angle": 0, "paint": "red"},
                    {"type": "circle", "x": 200, "y": 200, "radius": 30, "rotation_angle": 0, "paint": "blue"}
                ]

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
        elif canVas.draw_mode == "rectangle": 
            width = e.local_x - self.state.x
            height = e.local_y - self.state.y
            #self.draw_rectangle(self.state.x, self.state.y, width, height)
            #self.pan_shape_start(e)
            self.pan_storke_rect_update(e)
        elif canVas.draw_mode == "circle":
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

    def pan_end(self, e: ft.DragEndEvent):
        if canVas.draw_mode == "rectangle":
            self.finalize_rectangle()

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
    
    #pass
    def draw_rotated_rectangle(self, rect, angle):
        """長方形を回転して描画"""
    # 長方形の中心を計算
        #rect.rotation_angle += angle
        cx = rect.x + rect.width / 2
        cy = rect.y + rect.height / 2

    # 各頂点を計算
        #angle = rect.rotation_angle
        top_left = self.rotate_point(rect.x, rect.y, cx, cy, angle)
        top_right = self.rotate_point(rect.x + rect.width, rect.y, cx, cy, angle)
        bottom_left = self.rotate_point(rect.x, rect.y + rect.height, cx, cy, angle)
        bottom_right = self.rotate_point(rect.x + rect.width, rect.y + rect.height, cx, cy, angle)

    # 元の長方形を削除し、回転後の図形を追加
        rect.paint.color = "black"  # 回転中にわかりやすくするための色変更
        self.cp.shapes.remove(rect)  # 元の長方形を削除
        self.cp.shapes.append(
            cv.Line(*top_left, *top_right, paint=ft.Paint(color=rect.paint.color, stroke_width=rect.paint.stroke_width))
        )
        self.cp.shapes.append(
            cv.Line(*top_right, *bottom_right, paint=ft.Paint(color=rect.paint.color, stroke_width=rect.paint.stroke_width))
        )
        self.cp.shapes.append(
            cv.Line(*bottom_right, *bottom_left, paint=ft.Paint(color=rect.paint.color, stroke_width=rect.paint.stroke_width))
        )
        self.cp.shapes.append(
            cv.Line(*bottom_left, *top_left, paint=ft.Paint(color=rect.paint.color, stroke_width=rect.paint.stroke_width))
        )

        #self.cp.update()

    def rotate_point(self, x, y, cx, cy, angle):
        """点を中心点を基準に回転"""
        radians = math.radians(angle)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        nx = cos_a * (x - cx) - sin_a * (y - cy) + cx
        ny = sin_a * (x - cx) + cos_a * (y - cy) + cy
        return nx, ny

    def rotate_shape(self):
        for shape in self.cp.shapes:
            print("一つ足りないrotate_shape")
            #if isinstance(shape, cv.Rect):
            print("ここにきてるよrotateShape")
            self.draw_rotated_rectangle(shape, 5)
        self.cp.update()
    
    def pan_shape_start(self, e: ft.DragStartEvent):
        self.state.x = e.local_x
        self.state.y = e.local_y
        self.cp.shapes.append(None) # hogeオブジェクト，意味はない

    def pan_storke_rect_update(self, e: ft.DragUpdateEvent):
        self.cp.shapes.pop() # 先に描画された図形をポップして削除
        self.cp.shapes.append(
            cv.Rect(
                x=self.state.x,
                y=self.state.y,
                width=e.local_x - self.state.x,
                height=e.local_y - self.state.y,
                paint=ft.Paint(
                    color=canVas.color,
                    stroke_width=canVas.width,
                    style=ft.PaintingStyle("fill")
                )
            )
        )
        self.cp.update()
    
    def draw_rectangle(self, x, y, width, height):
        if self.current_rectangle is None:
            #self.current_rectangle = cv.Rect(
            #    x=x, y=y, width=width, height=height,
            #    paint=ft.Paint(color=canVas.color, stroke_width=canVas.width, style="stroke")
            #)
            self.cp.shapes.append(
                cv.Rect(
                x=x, y=y, width=width, height=height,
                paint=ft.Paint(color=canVas.color, stroke_width=canVas.width, style="fill")
                )
            )
            #self.cp.shapes.append(self.current_rectangle)
            self.cp.update()
            print("かきはじめかきおわり")
        else:
            self.current_rectangle.x = x
            self.current_rectangle.y = y
            self.current_rectangle.width = width
            self.current_rectangle.height = height
            #self.cp.shapes.append(self.current_rectangle)
            print("かいかき")
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
            self.cp.shapes.append(
                cv.Circle(
                x=x, y=y, radius=radius,
                paint=ft.Paint(color=canVas.color, stroke_width=canVas.width, style="fill")
                )
            )
            #self.current_circle = cv.Circle(
            #    x=x, y=y, radius=radius,
            #    paint=ft.Paint(color=canVas.color, stroke_width=canVas.width, style="fill")
            #)
            print("かきはじめかきおわり")
            #self.cp.shapes.append(self.current_circle)
        else:
            self.current_circle.x = x
            self.current_circle.y = y
            self.current_circle.radius = radius
            print("かきかき")
            self.current_circle.update()

        self.cp.update()

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
            width=800,
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