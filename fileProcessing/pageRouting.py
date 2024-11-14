import flet as ft
import start_viewVer

def main(page: ft.Page):
    startview = start_viewVer.startView(page)

    def route_change(handler):
        troute = ft.TemplateRoute(handler.route)
        page.views.clear()
        if troute.match("/startView"):
            page.views.append(startview.startView())
        elif troute.match("/view2"):
            page.views.append(startview.create_view2())
        page.update()

    # ルート変更時のロジック設定
    page.on_route_change = route_change

    # 初期表示
    page.go("/startView")


if __name__ == "__main__":
    ft.app(target=main)