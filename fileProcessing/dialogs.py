import flet as ft

class inputFolderNameDialog:
    inputFolderNameDialog = ft.AlertDialog(
        title=ft.Text("フォルダ名を入力してください"),
        modal=True,
        content=ft.TextField(),
        actions=[
            ft.TextButton("作成"),
            ft.TextButton("キャンセル")
        ]
    )

    def __init__(self, fun1, fun2):
        inputFolderNameDialog.inputFolderNameDialog.actions[0].on_click = fun1
        inputFolderNameDialog.inputFolderNameDialog.actions[1].on_click = fun2


class chooseContiNewDialog:
    chooseContiNewDialog = ft.CupertinoActionSheet(
        title=ft.Row([ft.Text("動画を作る")], alignment=ft.MainAxisAlignment.CENTER),
        message=ft.Row([ft.Text("作成方法を選んでください")], alignment=ft.MainAxisAlignment.CENTER),
        cancel=ft.CupertinoActionSheetAction(content=ft.Text("キャンセル")),
        actions=[
            ft.CupertinoActionSheetAction(content=ft.Text("新しく作る")),
            ft.CupertinoActionSheetAction(content=ft.Text("続きを作る")),
        ],
    )
    bottom_sheet = ft.CupertinoBottomSheet(chooseContiNewDialog)

    def __init__(self, fun1, fun2, fun3):
        chooseContiNewDialog.chooseContiNewDialog.cancel.on_click = fun1
        chooseContiNewDialog.chooseContiNewDialog.actions[0].on_click = fun2
        chooseContiNewDialog.chooseContiNewDialog.actions[1].on_click = fun3


class chooseWatchVideo:
    chooseDialog = ft.CupertinoActionSheet(
        title=ft.Row([ft.Text("動画を見る")], alignment=ft.MainAxisAlignment.CENTER),
        message=ft.Row([ft.Text("見る動画を選んでください")], alignment=ft.MainAxisAlignment.CENTER),
        cancel=ft.CupertinoActionSheetAction(content=ft.Text("キャンセル")),
        actions=[
            ft.CupertinoActionSheetAction(content=ft.Text("自分の動画を見る")),
            ft.CupertinoActionSheetAction(content=ft.Text("みんなの動画を見る")),
        ],
    )
    bottom_sheet = ft.CupertinoBottomSheet(chooseDialog)

    def __init__(self, fun1, fun2, fun3):
        chooseWatchVideo.chooseDialog.cancel.on_click = fun1
        chooseWatchVideo.chooseDialog.actions[0].on_click = fun2
        chooseWatchVideo.chooseDialog.actions[0].on_click = fun3


class emptyUploadList:
    def __init__(self, page: ft.Page):
        self.emptyDialog = ft.AlertDialog(
            title=ft.Text("アナウンス"),
            modal=True,
            content=ft.Text("作成された動画がありません"),
            actions=[
                ft.TextButton("了解しました", on_click=lambda e: page.close(self.emptyDialog))
            ]
        )


class chooseUploadVideo:
    def __init__(self, page: ft.Page):
        self.chooseDialog = ft.AlertDialog(
            title=ft.Text("アップロードする動画を選んでください"),
            modal=True,
            content=[
                ft.Checkbox()
            ],
            actions=[
                ft.TextButton("アップロード", on_click=lambda e: None),
                ft.TextButton("キャンセル", on_click=lambda e: page.close(self.chooseDialog))
            ]
        )