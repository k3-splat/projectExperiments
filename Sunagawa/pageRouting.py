import flet as ft
import start
import mainView
import videoPlayView
import projectRemoveView
import chooseProjectView

async def main(page: ft.Page):
    startview = start.startView(page)
    videoview = videoPlayView.videoPlay(page)
    mainview = mainView.mainView(page)

    def route_change(handler):
        troute = ft.TemplateRoute(handler.route)
        page.views.clear()
        if troute.match("/startView"):
            page.views.append(startview.startView())
        elif troute.match("/mainView"):
            page.views.append(mainview.makeView())
        elif troute.match("/videoPlayView"):
            page.views.append(videoview.makeView())
        elif troute.match("/removeView"):
            removelist = projectRemoveView.removeList(page)
            page.views.append(removelist.makeView())
        elif troute.match("/projectOpenView"):
            projectlist = chooseProjectView.projectList(page)
            page.views.append(projectlist.makeView())
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