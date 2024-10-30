import flet as ft

def main(page: ft.Page):
    # ページの基本設定
    page.title = "Video Thumbnails with Custom Icon and Username"
    page.scroll = "adaptive"
    page.padding = 10

    # サムネイルのデータ例（動画のタイトルとユーザー名を含む）
    videos = [
        {"title": "Video 1", "thumbnail": "https://via.placeholder.com/150", "username": "User1", "description": "This is Video 1"},
        {"title": "Video 2", "thumbnail": "https://via.placeholder.com/150", "username": "User2", "description": "This is Video 2"},
        {"title": "Video 3", "thumbnail": "https://via.placeholder.com/150", "username": "User3", "description": "This is Video 3"},
        {"title": "Video 4", "thumbnail": "https://via.placeholder.com/150", "username": "User4", "description": "This is Video 4"},
    ]

    # サムネイルをクリックしたときの処理
    def show_details(e):
        video = e.control.data
        page.dialog = ft.AlertDialog(
            title=ft.Text(video["title"]),
            content=ft.Text(video["description"]),
            on_dismiss=lambda e: page.update()
        )
        page.dialog.open = True
        page.update()

    # GridViewで2列レイアウトを作成
    grid = ft.GridView(
        expand=True,
        max_extent=page.width // 2 - 15,  # ページ幅に応じた2列表示
        child_aspect_ratio=1.0,  # 幅:高さの比率
        spacing=10,
        run_spacing=10,
    )

    # 動画サムネイルにアイコンとユーザー名を追加
    for video in videos:
        grid.controls.append(
            ft.Container(
                content=ft.Stack(
                    [
                        # サムネイル画像
                        ft.Image(src=video["thumbnail"], width=150, height=150, fit="cover"),

                        # 右下のアイコン (IMG_4007.JPGを使用)
                        ft.Container(
                            content=ft.Image(
                                src="IMG_4007.JPG",  # アイコン画像のパスを指定
                                width=30, height=30, fit="contain"
                            ),
                            alignment=ft.alignment.bottom_right,
                            padding=5
                        ),

                        # 左下に配置するユーザー名
                        ft.Container(
                            content=ft.Text(
                                video["username"], 
                                weight=ft.FontWeight.BOLD, 
                                size=14, 
                                color="black"
                            ),
                            alignment=ft.alignment.bottom_left,  # 左下に配置
                            padding=10  # 少し内側に寄せる
                        )
                    ]
                ),
                padding=5,
                border_radius=10,
                ink=True,
                bgcolor="white",  # 背景を白に設定
                on_click=show_details,
                data=video,  # 各コンテナにデータを保持
                border=ft.border.all(1, "gray")  # 枠線を追加
            )
        )

    # ページのリサイズに対応
    def on_resize(e):
        grid.max_extent = page.width // 2 - 15
        page.update()

    page.on_resize = on_resize  # リサイズイベントを登録

    # ページにGridViewを追加
    page.add(grid)

# Fletアプリケーションの開始
ft.app(target=main)
