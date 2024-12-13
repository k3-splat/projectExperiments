import flet as ft
import flet.canvas as cv

class State:
    x: float
    y: float

class canvasClass:
    color = ft.colors.BLACK
    stroke_width = 3
    canvasWidth = 800
    canvasHeight = 450

    @classmethod
    def setColor(cls, color):
        cls.color = color

    @classmethod
    def getColor(cls):
        return cls.color

    @classmethod
    def setStrokeWidth(cls, width):
        cls.stroke_width = width

    @classmethod
    def getStrokeWidth(cls):
        return cls.stroke_width
    
    @classmethod
    def setCnavasSize(cls, width, height):
        cls.canvasWidth = width
        cls.canvasHeight = height

    @classmethod
    def getCanvasSize(cls):
        return cls.canvasWidth, cls.canvasHeight

    def __init__(self):
        self.state = State()
        self.drawing = ft.GestureDetector(
            on_pan_start=self.pan_freestroke_start,
            on_pan_update=self.pan_freestroke_update,
            drag_interval=10
        )
        self.cp = cv.Canvas(
            content=self.drawing
        )

    def pan_freestroke_start(self, e: ft.DragStartEvent):
        self.state.x = e.local_x
        self.state.y = e.local_y

    def pan_freestroke_update(self, e: ft.DragUpdateEvent):
        self.cp.shapes.append(
            cv.Line(
                x1=self.state.x,
                y1=self.state.y,
                x2=e.local_x,
                y2=e.local_y,
                paint=ft.Paint(
                    color=canvasClass.getColor(),
                    stroke_width=canvasClass.getStrokeWidth()
                )
            )
        )
        self.cp.update()
        self.state.x = e.local_x
        self.state.y = e.local_y

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
                    color=canvasClass.getColor(),
                    stroke_width=canvasClass.getStrokeWidth(),
                    style=ft.PaintingStyle("stroke")
                )
            )
        )
        self.cp.update()

    def makeCanvas(self):
        width, height = canvasClass.getCanvasSize()

        return ft.Container(
            self.cp,
            border_radius=0,
            width=width, # アスペクト比に準拠
            height=height
        )