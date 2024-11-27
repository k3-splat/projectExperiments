import flet as ft
import start
import mainView
import videoPlayView

async def main(page: ft.Page):
    startview = start.startView(page)
    videoview = videoPlayView.videoPlay()

    def route_change(handler):
        troute = ft.TemplateRoute(handler.route)
        page.views.clear()
        if troute.match("/startView"):
            page.views.append(startview.startView())
        elif troute.match("/MainPage"):
            page.views.append(mainView.main(page))
        elif troute.match("/videoPlay"):
            page.views.append(videoview.makeView())
        page.update()

    # ルート変更時のロジック設定
    page.on_route_change = route_change

    # 初期表示
    page.go("/startView")

    # 非同期タスクを開始
    await startview.update_time()

if __name__ == "__main__":
    # 非同期関数をターゲットに指定
    ft.app(target=main, assets_dir="assets")