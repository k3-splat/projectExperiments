import flet as ft
import start

async def main(page: ft.Page):
    startview = start.startView(page)

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

    # 非同期タスクを開始
    await startview.update_time()

if __name__ == "__main__":
    # 非同期関数をターゲットに指定
    ft.app(target=main)