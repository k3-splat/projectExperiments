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
    def setColor(cls, color: ft.colors):
        cls.color = color

    @classmethod
    def setStrokeWidth(cls, width: int):
        cls.stroke_width = width

    @classmethod
    def getCanvasSize(cls):
        return cls.canvasWidth, cls.canvasHeight

    def __init__(self):
        self.state = State()
        self.drawing = ft.GestureDetector(
            on_pan_start=self.pan_start,
            on_pan_update=self.pan_update,
            drag_interval=10
        )
        self.cp = cv.Canvas(
            content=self.drawing
        )

    def pan_start(self, e: ft.DragStartEvent):
        self.state.x = e.local_x
        self.state.y = e.local_y

    def pan_update(self, e: ft.DragUpdateEvent):
        self.cp.shapes.append(
            cv.Line(
                self.state.x, self.state.y, e.local_x, e.local_y, paint=ft.Paint(color=canvasClass.color, stroke_width=canvasClass.stroke_width)
            )
        )
        self.cp.update()
        self.state.x = e.local_x
        self.state.y = e.local_y

    def draw_rectangle(self, x, y, width, height):
        """Draws a rectangle on the canvas."""
        self.cp.shapes.append(
            cv.Rect(
                x=x, y=y, width=width, height=height,
                paint=ft.Paint(color=canvasClass.color, stroke_width=canvasClass.stroke_width, style="stroke")
            )
        )
        self.cp.update()

    def draw_circle(self, x, y, radius):
        """Draws a circle on the canvas."""
        self.cp.shapes.append(
            cv.Circle(
                x=x, y=y, radius=radius,
                paint=ft.Paint(color=canvasClass.color, stroke_width=canvasClass.stroke_width, style="stroke")
            )
        )
        self.cp.update()

    def draw_oval(self, x, y, width, height):
        """Draws an oval on the canvas."""
        self.cp.shapes.append(
            cv.Oval(
                x=x, y=y, width=width, height=height,
                paint=ft.Paint(color=canvasClass.color, stroke_width=canvasClass.stroke_width, style="stroke")
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