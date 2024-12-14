import flet as ft
import flet.canvas as cv

class State:
    x: float
    y: float

state = State()

def main(page: ft.Page):
    page.title = "Flet Brush"

    def pan_stroke_start(e: ft.DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y

    def pan_rect_start(e: ft.DragStartEvent):
        state.x = e.local_x
        state.y = e.local_y
        cp.shapes.append(None) # hogeオブジェクト，意味はない

    def pan_update(e: ft.DragUpdateEvent):
        cp.shapes.append(
            cv.Line(
                state.x, state.y, e.local_x, e.local_y, paint=ft.Paint(stroke_width=3)
            )
        )
        cp.update()
        state.x = e.local_x
        state.y = e.local_y
        
    def pan_rect_update(e: ft.DragUpdateEvent):
        cp.shapes.pop() # 先に描画された図形をポップして削除
        cp.shapes.append(
            cv.Rect(
                state.x, state.y, e.local_x - state.x, e.local_y - state.y, paint=ft.Paint(style=ft.PaintingStyle("stroke"))
            )
        )
        cp.update()

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
            on_pan_start=pan_rect_start,
            on_pan_update=pan_rect_update,
            drag_interval=10,
        ),
        expand=False,
    )

    page.add(
        ft.Container(
            cp,
            border_radius=5,
            width=float("inf"),
            expand=True,
        )
    )


ft.app(main)