import flet as ft

def main(page: ft.Page):
    import flet as ft
import flet.canvas as cv

class State:
    x: float
    y: float

state = State()

def main(page: ft.Page):
    page.title = "Flet Brush"

    def pan_start(e: ft.DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y

    def pan_update(e: ft.DragUpdateEvent):
        cp.shapes.append(
            cv.Line(
                state.x, state.y, e.local_x, e.local_y, paint=ft.Paint(stroke_width=3)
            )
        )
        cp.update()
        state.x = e.local_x
        state.y = e.local_y

    cp = cv.Canvas(
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
            on_pan_start=pan_start,
            on_pan_update=pan_update,
            drag_interval=10,
        ),
        expand=False,
    )

    def on_pan_update2(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    gd1 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=10,
        on_vertical_drag_update=on_pan_update2,
        left=100,
        top=100,
        content=ft.Container(bgcolor=ft.colors.BLUE, width=50, height=50),
    )

    page.add( ft.Stack([
        ft.Container(
            cp,
            border_radius=5,
            width=float("inf"),
            expand=True,
        ),
        gd1
    ], width=1000, height=500))

ft.app(main)