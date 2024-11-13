import flet as ft
from flet import(
    AlertDialog,
    Text,
    TextField,
    TextButton
)
from fileLoad import(
    mkdir
)

class inputFolderNameDialog:
    mkdir_dlg = AlertDialog(
        title=Text("フォルダ名を入力してください"),
        modal=True,
        content=TextField(),
        actions=[
            TextButton("作成", on_click=lambda e: None),
            TextButton("キャンセル", on_click=lambda e: None)
        ]
    )

    def __init__(self, fun1, fun2):
        inputFolderNameDialog.mkdir_dlg.actions[0].on_click = fun1
        inputFolderNameDialog.mkdir_dlg.actions[1].on_click = fun2

class chooseContiNewDialog:
    choose_dialog = ft.CupertinoActionSheet(
        title=ft.Row([ft.Text("動画を作る")], alignment=ft.MainAxisAlignment.CENTER),
        message=ft.Row([ft.Text("作成方法を選んでください")], alignment=ft.MainAxisAlignment.CENTER),
        cancel=ft.CupertinoActionSheetAction(
            content=ft.Text("キャンセル"),
            on_click=lambda e: None
        ),
        actions=[
            ft.CupertinoActionSheetAction(
                content=ft.Text("新しく作る"),
                on_click=lambda e: None
            ),
            ft.CupertinoActionSheetAction(
                content=ft.Text("続きを作る"),
                on_click=lambda e: None
            ),
        ],
    )

    def __init__(self, page: ft.Page):
        make_directory = mkdir()

        inputfoldernamedialog = inputFolderNameDialog(
            lambda e: make_directory.make_directory(page, inputfoldernamedialog.mkdir_dlg), #ボタンを押すという「イベント」なので、イベントオブジェクトeを渡す
            lambda e: page.close(inputfoldernamedialog.mkdir_dlg)
        )

        self.get_directory_dialog = ft.FilePicker(on_result=lambda e: make_directory.input_directory_path(page, e, inputfoldernamedialog.mkdir_dlg))

        self.bottom_sheet = ft.CupertinoBottomSheet(chooseContiNewDialog.choose_dialog)
        
        chooseContiNewDialog.choose_dialog.cancel.on_click = lambda e: page.close(self.bottom_sheet)
        chooseContiNewDialog.choose_dialog.actions[0].on_click = lambda e: self.get_directory_dialog.get_directory_path(dialog_title="新しく作る")
        chooseContiNewDialog.choose_dialog.actions[1].on_click = lambda e: None

class chooseWatchVideo:
    chooseDialog = ft.CupertinoActionSheet(
        title=ft.Row([ft.Text("動画を見る")], alignment=ft.MainAxisAlignment.CENTER),
        message=ft.Row([ft.Text("見る動画を選んでください")], alignment=ft.MainAxisAlignment.CENTER),
        cancel=ft.CupertinoActionSheetAction(
            content=ft.Text("キャンセル"),
            on_click=lambda e: None
        ),
        actions=[
            ft.CupertinoActionSheetAction(
                content=ft.Text("自分の動画を見る"),
                on_click=lambda e: None
            ),
            ft.CupertinoActionSheetAction(
                content=ft.Text("みんなの動画を見る"),
                on_click=lambda e: None
            ),
        ],
    )

    def __init__(self, page: ft.Page):
        self.bottom_sheet = ft.CupertinoBottomSheet(chooseWatchVideo.chooseDialog)

        chooseWatchVideo.chooseDialog.cancel.on_click = lambda e: page.close(self.bottom_sheet)