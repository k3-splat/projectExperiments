import flet as ft
import flet.canvas as cv

class State:
    x: float
    y: float

class canVas:
    def __init__(self):
        self.state = State()
        self.cp = cv.Canvas(
            [
                cv.Fill(
                    ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            (0, 0), (600, 600), colors=[ft.colors.CYAN_50, ft.colors.GREY]
                        )
                    )
                ),
            ],
            content=ft.GestureDetector(
                on_pan_start=self.pan_start,
                on_pan_update=self.pan_update,
                drag_interval=10,
            ),
            expand=False,
        )

    def pan_start(self, e: ft.DragStartEvent):
        self.state.x = e.local_x
        self.state.y = e.local_y

    def pan_update(self, e: ft.DragUpdateEvent):
        self.cp.shapes.append(
            cv.Line(
                self.state.x, self.state.y, e.local_x, e.local_y, paint=ft.Paint(stroke_width=3)
            )
        )
        self.cp.update()
        self.state.x = e.local_x
        self.state.y = e.local_y

    def makeCanvas(self):
        return ft.Container(
            self.cp,
            border_radius=5,
            width=float("inf")
        )


if __name__=="__main__":
    pass