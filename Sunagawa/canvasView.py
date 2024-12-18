import flet as ft
import flet.canvas as cv
import math

class State:
    x: float
    y: float

class canvasClass:
    color = ft.colors.BLACK
    stroke_width = 3
    canvasWidth = 1000
    canvasHeight = 563
    draw_mode = "free"
    eraser_size = 10

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
    
    @classmethod
    def setEraser_size(cls, size):
        cls.eraser_size = size

    @classmethod
    def getEraser_size(cls):
        return cls.eraser_size

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

        elif canvasClass.draw_mode == "stroke_line":
            self.cp.content.on_pan_start = self.pan_shape_start
            self.cp.content.on_pan_update = self.pan_stroke_line_update

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

        elif canvasClass.draw_mode == "oval_fill":
            self.cp.content.on_pan_start = self.pan_shape_start
            self.cp.content.on_pan_update = self.pan_oval_fill_update

        elif canvasClass.draw_mode == "oval_stroke":
            self.cp.content.on_pan_start = self.pan_shape_start
            self.cp.content.on_pan_update = self.pan_oval_stroke_update

        elif canvasClass.draw_mode == "scaling":
            self.cp.content.on_pan_start = self.pan_scaling_start
            self.cp.content.on_pan_update = self.pan_scaling_update

        elif canvasClass.draw_mode == "Small":
            pass

        elif canvasClass.draw_mode == "eraser":
            self.cp.content.on_pan_start = self.pan_normal_start
            self.cp.content.on_pan_update = self.pan_eraser_update

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
        for shape in self.cp.shapes:
            if type(shape) is cv.Rect:
                if shape.paint.style == ft.PaintingStyle("fill"):
                    if shape.width < 0 and shape.height < 0:
                        if shape.x + shape.width <= e.local_x <= shape.x and shape.y + shape.height <= e.local_y <= shape.y:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "rect_fill"

                    elif shape.width < 0:
                        if shape.x + shape.width <= e.local_x <= shape.x and shape.y <= e.local_y <= shape.y + shape.height:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "rect_fill"

                    elif shape.height < 0:
                        if shape.x <= e.local_x <= shape.x + shape.width and shape.y + shape.height <= e.local_y <= shape.y:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "rect_fill"

                    else:
                        if shape.x <= e.local_x <= shape.x + shape.width and shape.y <= e.local_y <= shape.y + shape.height:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "rect_fill"

                elif shape.paint.style == ft.PaintingStyle("stroke"):
                    if shape.width < 0 and shape.height < 0:
                        if shape.x + shape.width <= e.local_x <= shape.x and shape.y + shape.height <= e.local_y <= shape.y:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "rect_stroke"

                    elif shape.width < 0:
                        if shape.x + shape.width <= e.local_x <= shape.x and shape.y <= e.local_y <= shape.y + shape.height:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "rect_stroke"

                    elif shape.height < 0:
                        if shape.x <= e.local_x <= shape.x + shape.width and shape.y + shape.height <= e.local_y <= shape.y:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "rect_stroke"

                    else:
                        if shape.x <= e.local_x <= shape.x + shape.width and shape.y <= e.local_y <= shape.y + shape.height:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "rect_stroke"

            if type(shape) is cv.Circle:
                if shape.paint.style == ft.PaintingStyle("fill"):
                    if shape.x - shape.radius <= e.local_x <= shape.x + shape.radius or shape.y - shape.radius <= e.local_y <= shape.y + shape.radius:
                        self.scaling_index = self.cp.shapes.index(shape)
                        self.scaling_x = shape.x
                        self.scaling_y = shape.y
                        self.type = "circle_fill"

                if shape.paint.style == ft.PaintingStyle("stroke"):
                    if shape.x - shape.radius <= e.local_x <= shape.x + shape.radius or shape.y - shape.radius <= e.local_y <= shape.y + shape.radius:
                        self.scaling_index = self.cp.shapes.index(shape)
                        self.scaling_x = shape.x
                        self.scaling_y = shape.y
                        self.type = "circle_stroke"

            if type(shape) is cv.Oval:
                if shape.paint.style == ft.PaintingStyle("fill"):
                    if shape.width < 0 and shape.height < 0:
                        if shape.x + shape.width <= e.local_x <= shape.x and shape.y + shape.height <= e.local_y <= shape.y:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "oval_fill"

                    elif shape.width < 0:
                        if shape.x + shape.width <= e.local_x <= shape.x and shape.y <= e.local_y <= shape.y + shape.height:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "oval_fill"

                    elif shape.height < 0:
                        if shape.x <= e.local_x <= shape.x + shape.width and shape.y + shape.height <= e.local_y <= shape.y:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "oval_fill"

                    else:
                        if shape.x <= e.local_x <= shape.x + shape.width and shape.y <= e.local_y <= shape.y + shape.height:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "oval_fill"

                elif shape.paint.style == ft.PaintingStyle("stroke"):
                    if shape.width < 0 and shape.height < 0:
                        if shape.x + shape.width <= e.local_x <= shape.x and shape.y + shape.height <= e.local_y <= shape.y:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "oval_stroke"

                    elif shape.width < 0:
                        if shape.x + shape.width <= e.local_x <= shape.x and shape.y <= e.local_y <= shape.y + shape.height:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "oval_stroke"

                    elif shape.height < 0:
                        if shape.x <= e.local_x <= shape.x + shape.width and shape.y + shape.height <= e.local_y <= shape.y:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "oval_stroke"

                    else:
                        if shape.x <= e.local_x <= shape.x + shape.width and shape.y <= e.local_y <= shape.y + shape.height:
                            self.scaling_index = self.cp.shapes.index(shape)
                            self.scaling_x = shape.x
                            self.scaling_y = shape.y
                            self.scaling_width = shape.width
                            self.ratio = shape.height / shape.width
                            self.type = "oval_stroke"

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

    def pan_stroke_line_update(self, e:ft.DragUpdateEvent):
        self.cp.shapes.pop()
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

    def pan_oval_fill_update(self, e: ft.DragUpdateEvent):
        self.cp.shapes.pop()
        self.cp.shapes.append(
            cv.Oval(
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

    def pan_oval_stroke_update(self, e: ft.DragUpdateEvent):
        self.cp.shapes.pop()
        self.cp.shapes.append(
            cv.Oval(
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

    def pan_scaling_update(self, e: ft.DragUpdateEvent):
        self.cp.shapes.pop(self.scaling_index)
        if self.type == "rect_fill":
            if self.scaling_width >= 0:
                width = max(abs(e.local_x - self.scaling_x), abs(e.local_y - self.scaling_y))

            else:
                width = -max(abs(e.local_x - self.scaling_x), abs(e.local_y - self.scaling_y))

            self.cp.shapes.insert(
                self.scaling_index,
                cv.Rect(
                    x=self.scaling_x,
                    y=self.scaling_y,
                    width=width,
                    height=width * self.ratio,
                    paint=ft.Paint(
                        color=canvasClass.getColor(),
                        stroke_width=canvasClass.getStrokeWidth(),
                        style=ft.PaintingStyle("fill")
                    )
                )
            )

        elif self.type == "rect_stroke":
            if self.scaling_width >= 0:
                width = max(abs(e.local_x - self.scaling_x), abs(e.local_y - self.scaling_y))

            else:
                width = -max(abs(e.local_x - self.scaling_x), abs(e.local_y - self.scaling_y))

            self.cp.shapes.insert(
                self.scaling_index,
                cv.Rect(
                    x=self.scaling_x,
                    y=self.scaling_y,
                    width=width,
                    height=width * self.ratio,
                    paint=ft.Paint(
                        color=canvasClass.getColor(),
                        stroke_width=canvasClass.getStrokeWidth(),
                        style=ft.PaintingStyle("stroke")
                    )
                )
            )

        elif self.type == "circle_fill":
            radius = max(abs(e.local_x - self.scaling_x), abs(e.local_y - self.scaling_y))

            self.cp.shapes.insert(
                self.scaling_index,
                cv.Circle(
                    x=self.scaling_x,
                    y=self.scaling_y,
                    radius=radius,
                    paint=ft.Paint(
                        color=canvasClass.getColor(),
                        stroke_width=canvasClass.getStrokeWidth(),
                        style=ft.PaintingStyle("fill")
                    )
                )
            )

        elif self.type == "circle_stroke":
            radius = max(abs(e.local_x - self.scaling_x), abs(e.local_y - self.scaling_y))

            self.cp.shapes.insert(
                self.scaling_index,
                cv.Circle(
                    x=self.scaling_x,
                    y=self.scaling_y,
                    radius=radius,
                    paint=ft.Paint(
                        color=canvasClass.getColor(),
                        stroke_width=canvasClass.getStrokeWidth(),
                        style=ft.PaintingStyle("stroke")
                    )
                )
            )

        elif self.type == "oval_fill":
            if self.scaling_width >= 0:
                width = max(abs(e.local_x - self.scaling_x), abs(e.local_y - self.scaling_y))

            else:
                width = -max(abs(e.local_x - self.scaling_x), abs(e.local_y - self.scaling_y))

            self.cp.shapes.insert(
                self.scaling_index,
                cv.Oval(
                    x=self.scaling_x,
                    y=self.scaling_y,
                    width=width,
                    height=width * self.ratio,
                    paint=ft.Paint(
                        color=canvasClass.getColor(),
                        stroke_width=canvasClass.getStrokeWidth(),
                        style=ft.PaintingStyle("fill")
                    )
                )
            )

        elif self.type == "oval_stroke":
            if self.scaling_width >= 0:
                width = max(abs(e.local_x - self.scaling_x), abs(e.local_y - self.scaling_y))

            else:
                width = -max(abs(e.local_x - self.scaling_x), abs(e.local_y - self.scaling_y))

            self.cp.shapes.insert(
                self.scaling_index,
                cv.Oval(
                    x=self.scaling_x,
                    y=self.scaling_y,
                    width=width,
                    height=width * self.ratio,
                    paint=ft.Paint(
                        color=canvasClass.getColor(),
                        stroke_width=canvasClass.getStrokeWidth(),
                        style=ft.PaintingStyle("stroke")
                    )
                )
            )

        self.cp.update()

    def pan_eraser_update(self, e: ft.DragUpdateEvent):
        eraser_points = self.get_points_within_radius(self.state.x, self.state.y, canvasClass.getEraser_size())
        
        for eraser_point in eraser_points:
            x, y = eraser_point
            for shape in self.cp.shapes:
                if type(shape) is cv.Line:
                    if shape.x1 - 5 <= x <= shape.x1 + 5 and shape.y1 - 5 <= y <= shape.y1 + 5 or shape.x2 - 5 <= x <= shape.x2 + 5 and shape.y2 - 5 <= y <= shape.y2 + 5:
                        self.cp.shapes.remove(shape)

                if type(shape) is cv.Rect:
                    if shape.width < 0 and shape.height < 0:
                        if shape.x + shape.width <= x <= shape.x and shape.y + shape.height <= y <= shape.y:
                            self.cp.shapes.remove(shape)

                    elif shape.width < 0:
                        if shape.x + shape.width <= x <= shape.x and shape.y <= y <= shape.y + shape.height:
                            self.cp.shapes.remove(shape)

                    elif shape.height < 0:
                        if shape.x <= x <= shape.x + shape.width and shape.y + shape.height <= y <= shape.y:
                            self.cp.shapes.remove(shape)

                    else:
                        if shape.x <= e.local_x <= x + shape.width and shape.y <= y <= shape.y + shape.height:
                            self.cp.shapes.remove(shape)

                if type(shape) is cv.Circle:
                    if shape.x - shape.radius <= x <= shape.x + shape.radius and shape.y - shape.radius <= y <= shape.y + shape.radius:
                        self.cp.shapes.remove(shape)

                if type(shape) is cv.Oval:
                    if shape.width < 0 and shape.height < 0:
                        if shape.x + shape.width <= x <= shape.x and shape.y + shape.height <= y <= shape.y:
                            self.cp.shapes.remove(shape)

                    elif shape.width < 0:
                        if shape.x + shape.width <= x <= shape.x and shape.y <= y <= shape.y + shape.height:
                            self.cp.shapes.remove(shape)

                    elif shape.height < 0:
                        if shape.x <= x <= shape.x + shape.width and shape.y + shape.height <= y <= shape.y:
                            self.cp.shapes.remove(shape)

                    else:
                        if shape.x <= e.local_x <= x + shape.width and shape.y <= y <= shape.y + shape.height:
                            self.cp.shapes.remove(shape)

        self.cp.update()
        self.state.x = e.local_x
        self.state.y = e.local_y

    def get_points_within_radius(self, cx, cy, r):
        points = []
        for x in range(int(cx - r), int(cx + r + 1)):  # xの範囲
            for y in range(int(cy - r), int(cy + r + 1)):  # yの範囲
                if (x - cx)**2 + (y - cy)**2 <= r**2:  # 範囲判定
                    points.append((x, y))
        return points
    
    def makeCanvas(self):
        width, height = canvasClass.getCanvasSize()

        return ft.Container(
            self.cp,
            border_radius=0,
            width=width, # アスペクト比に準拠
            height=height
        )