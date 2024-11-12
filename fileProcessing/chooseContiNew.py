import flet as ft
from fileLoad import(
    mkdir
)

class chooseContiNew:
    def __init__(self, page: ft.Page):
        make_directory = mkdir(page)
        get_directory_dialog = ft.FilePicker(on_result=make_directory.get_directory_path)

        mkdir.mkdir_dlg.actions[0].on_click = make_directory.make_directory
        mkdir.mkdir_dlg.actions[1].on_click = lambda e: page.close(mkdir.mkdir_dlg)

        self.choose_dialog = ft.CupertinoActionSheet(
            title=ft.Row([ft.Text("動画を作る")], alignment=ft.MainAxisAlignment.CENTER),
            message=ft.Row([ft.Text("作成方法を選んでください")], alignment=ft.MainAxisAlignment.CENTER),
            cancel=ft.CupertinoActionSheetAction(
                content=ft.Text("Cancel"),
                on_click=page.close(self.choose_dialog),
            ),
            actions=[
                ft.CupertinoActionSheetAction(
                    content=ft.Text("新しく作る"),
                    is_default_action=True,
                    on_click=lambda _: get_directory_dialog.get_directory_path(dialog_title="フォルダーを選択"),
                ),
                ft.CupertinoActionSheetAction(
                    content=ft.Text("続きを作る"),
                    on_click=lambda e: None,
                ),
            ],
        )