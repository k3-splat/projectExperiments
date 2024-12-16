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
    draw_mode = "free"

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
    def setCanvasSize(cls, width, height):
        cls.canvasWidth = width
        cls.canvasHeight = height

    @classmethod
    def getCanvasSize(cls):
        return cls.canvasWidth, cls.canvasHeight
    
    @classmethod
    def setDrawMode(cls, mode: str):
        cls.draw_mode = mode

    @classmethod
    def getDrawMode(cls):
        return cls.draw_mode

    def __init__(self):
        self.state = State()
        self.cp = cv.Canvas(
            content=ft.GestureDetector(
                on_pan_start=self.pan_normal_start,
                on_pan_update=self.pan_free_update,
                drag_interval=10
            )
        )

    def modeChange(self):
        if canvasClass.draw_mode == "free":  # 自由描画モード
            self.cp.content.on_pan_start = self.pan_normal_start
            self.cp.content.on_pan_update = self.pan_free_update

        elif canvasClass.draw_mode == "rectangle_fill": 
            self.cp.content.on_pan_start = self.pan_shape_start
            self.cp.content.on_pan_update = self.pan_rectangle_fill_update

        elif canvasClass.draw_mode == "rectangle_stroke": 
            self.cp.content.on_pan_start = self.pan_shape_start
            self.cp.content.on_pan_update = self.pan_rectangle_stroke_update

        elif canvasClass.draw_mode == "circle_fill":
            self.cp.content.on_pan_start = self.pan_shape_start
            self.cp.content.on_pan_update = self.pan_circle_fill_update

        elif canvasClass.draw_mode == "circle_stroke":
            self.cp.content.on_pan_start = self.pan_shape_start
            self.cp.content.on_pan_update = self.pan_circle_stroke_update

        elif canvasClass.draw_mode == "scaling":
            self.cp.content.on_pan_start = self.pan_scaling_start
            self.cp.content.on_pan_update = self.pan_scaling_update

        elif canvasClass.draw_mode == "Small":
            pass

        elif canvasClass.draw_mode == "eraser":
            pass

    def pan_normal_start(self, e: ft.DragStartEvent):
        self.state.x = e.local_x
        self.state.y = e.local_y

    def pan_shape_start(self, e:ft.DragStartEvent):
        self.state.x = e.local_x
        self.state.y = e.local_y
        self.cp.shapes.append(cv.Points(
            points=[ft.Offset(e.local_x, e.local_y)],
            point_mode=cv.PointMode.POINTS
        ))

    def pan_scaling_start(self, e: ft.DragStartEvent):
        self.state.x = e.local_x
        self.state.y = e.local_y
        indexList = []
        self.cp.content.mouse_corsor = ft.MouseCursor.RESIZE_UP_LEFT_DOWN_RIGHT

        for shape in self.cp.shapes:
            if type(shape) is cv.Rect:
                if shape.paint.style == "fill":
                    if shape.width < 0 and shape.height < 0:
                        if shape.x + shape.width <= e.local_x <= shape.x and shape.y + shape.height <= e.local_y <= shape.y:
                            indexList.append(self.cp.shapes.index(shape))

                    elif shape.width < 0:
                        if shape.x + shape.width <= e.local_x <= shape.x and shape.y <= e.local_y <= shape.y + shape.height:
                            indexList.append(self.cp.shapes.index(shape))

                    elif shape.height < 0:
                        if shape.x <= e.local_x <= shape.x + shape.width and shape.y + shape.height <= e.local_y <= shape.y:
                            indexList.append(self.cp.shapes.index(shape))

                    else:
                        if shape.x <= e.local_x <= shape.x + shape.width and shape.y <= e.local_y <= shape.y + shape.height:
                            indexList.append(self.cp.shapes.index(shape))

        print(indexList)

    def pan_free_update(self, e: ft.DragUpdateEvent):
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

    def pan_rectangle_fill_update(self, e:ft.DragUpdateEvent):
        self.cp.shapes.pop()
        self.cp.shapes.append(
            cv.Rect(
                x=self.state.x,
                y=self.state.y,
                width=e.local_x - self.state.x,
                height=e.local_y - self.state.y,
                paint=ft.Paint(
                    color=canvasClass.getColor(),
                    stroke_width=canvasClass.getStrokeWidth(),
                    style=ft.PaintingStyle("fill")
                )
            )
        )
        self.cp.update()

    def pan_rectangle_stroke_update(self, e:ft.DragUpdateEvent):
        self.cp.shapes.pop()
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

    def pan_circle_fill_update(self, e: ft.DragUpdateEvent):
        self.cp.shapes.pop()
        self.cp.shapes.append(
            cv.Circle(
                x=self.state.x,
                y=self.state.y,
                radius=max(abs(e.local_x - self.state.x), abs(e.local_y - self.state.y)),
                paint=ft.Paint(
                    color=canvasClass.getColor(),
                    stroke_width=canvasClass.getStrokeWidth(),
                    style=ft.PaintingStyle("fill")
                )
            )
        )
        self.cp.update()

    def pan_circle_stroke_update(self, e:ft.DragUpdateEvent):
        self.cp.shapes.pop()
        self.cp.shapes.append(
            cv.Circle(
                x=self.state.x,
                y=self.state.y,
                radius=max(abs(e.local_x - self.state.x), abs(e.local_y - self.state.y)),
                paint=ft.Paint(
                    color=canvasClass.getColor(),
                    stroke_width=canvasClass.getStrokeWidth(),
                    style=ft.PaintingStyle("stroke")
                )
            )
        )
        self.cp.update()

    def pan_scaling_update(self, e: ft.DragUpdateEvent):
        self.cp.shapes.pop(self.scaling_index)
        self.cp.shapes.insert(
            self.scaling_index,
            cv.Rect(
                x=self.scaling_x,
                y=self.scaling_y,
                width=e.local_x - self.scaling_x,
                height=e.local_y - self.scaling_y,
                paint=ft.Paint(
                    color=canvasClass.getColor(),
                    stroke_width=canvasClass.getStrokeWidth(),
                    style=ft.PaintingStyle("fill")
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