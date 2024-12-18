import flet as ft

class inputFolderNameDialog:
    def __init__(self, fun1, fun2):
        self.inputFolderNameDialog = ft.AlertDialog(
            title=ft.Text("フォルダ名を入力してください"),
            modal=True,
            content=ft.TextField(),
            actions=[
                ft.TextButton("作成"),
                ft.TextButton("キャンセル")
            ]
        )

        self.inputFolderNameDialog.actions[0].on_click = fun1
        self.inputFolderNameDialog.actions[1].on_click = fun2


class inputPageDialog:
    def __init__(self, fun1, fun2):
        self.inputPageDialog = ft.AlertDialog(
            title=ft.Text("追加するページを入力してください"),
            modal=True,
            content=ft.TextField(),
            actions=[
                ft.TextButton("追加"),
                ft.TextButton("キャンセル")
            ]
        )

        self.inputPageDialog.actions[0].on_click = fun1
        self.inputPageDialog.actions[1].on_click = fun2


class inputTimingDialog:
    def __init__(self, fun1, fun2):
        self.inputTimingDialog = ft.AlertDialog(
            title=ft.Text("追加する時間を入力してください"),
            modal=True,
            content=ft.TextField(),
            actions=[
                ft.TextButton("追加"),
                ft.TextButton("キャンセル")
            ]
        )

        self.inputTimingDialog.actions[0].on_click = fun1
        self.inputTimingDialog.actions[1].on_click = fun2


class minnanoDialog:
    def __init__(self, fun1):
        self.minnanoDialog = ft.AlertDialog(
            title=ft.Text("Attention"),
            modal=True,
            content=ft.Text("ブラウザを起動します"),
            actions=[
                ft.TextButton("了解しました")
            ]
        )

        self.minnanoDialog.actions[0].on_click = fun1


class inputFPSNameDialog:
    def __init__(self, fun1, fun2):
        self.inputFPSDialog = ft.AlertDialog(
            title=ft.Text("FPSを入力してください"),
            modal=True,
            content=ft.TextField(),
            actions=[
                ft.TextButton("作成"),
                ft.TextButton("キャンセル")
            ]
        )

        self.inputFPSDialog.actions[0].on_click = fun1
        self.inputFPSDialog.actions[1].on_click = fun2


class chooseContiNewDialog:
    def __init__(self, fun1, fun2, fun3):
        chooseContiNewDialog = ft.CupertinoActionSheet(
            title=ft.Row([ft.Text("動画を作る")], alignment=ft.MainAxisAlignment.CENTER),
            message=ft.Row([ft.Text("作成方法を選んでください")], alignment=ft.MainAxisAlignment.CENTER),
            cancel=ft.CupertinoActionSheetAction(content=ft.Text("キャンセル")),
            actions=[
                ft.CupertinoActionSheetAction(content=ft.Text("新しく作る")),
                ft.CupertinoActionSheetAction(content=ft.Text("続きを作る"))
            ],
        )
        self.bottom_sheet = ft.CupertinoBottomSheet(chooseContiNewDialog)

        chooseContiNewDialog.cancel.on_click = fun1
        chooseContiNewDialog.actions[0].on_click = fun2
        chooseContiNewDialog.actions[1].on_click = fun3


class chooseWatchVideo:
    def __init__(self, fun1, fun2, fun3):
        chooseDialog = ft.CupertinoActionSheet(
            title=ft.Row([ft.Text("動画を見る")], alignment=ft.MainAxisAlignment.CENTER),
            message=ft.Row([ft.Text("見る動画を選んでください")], alignment=ft.MainAxisAlignment.CENTER),
            cancel=ft.CupertinoActionSheetAction(content=ft.Text("キャンセル")),
            actions=[
                ft.CupertinoActionSheetAction(content=ft.Text("自分の動画を見る")),
                ft.CupertinoActionSheetAction(content=ft.Text("みんなの動画を見る")),
            ],
        )
        self.bottom_sheet = ft.CupertinoBottomSheet(chooseDialog)

        chooseDialog.cancel.on_click = fun1
        chooseDialog.actions[0].on_click = fun2
        chooseDialog.actions[1].on_click = fun3


class manageFolders:
    def __init__(self, fun1, fun2, fun3):
        chooseDialog = ft.CupertinoActionSheet(
            title=ft.Row([ft.Text("管理する")], alignment=ft.MainAxisAlignment.CENTER),
            message=ft.Row([ft.Text("何を管理しますか？")], alignment=ft.MainAxisAlignment.CENTER),
            cancel=ft.CupertinoActionSheetAction(content=ft.Text("キャンセル")),
            actions=[
                ft.CupertinoActionSheetAction(content=ft.Text("プロジェクトを管理する")),
                ft.CupertinoActionSheetAction(content=ft.Text("作った動画を管理する")),
            ],
        )
        self.bottom_sheet = ft.CupertinoBottomSheet(chooseDialog)

        chooseDialog.cancel.on_click = fun1
        chooseDialog.actions[0].on_click = fun2
        chooseDialog.actions[1].on_click = fun3


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

class AttentionRemove:
    def __init__(self, fun1, fun2):
        self.attentionDialog = ft.AlertDialog(
            title=ft.Text("Attention!"),
            modal=False,
            content=ft.Text("本当に削除してもよろしいですか？"),
            actions=[
                ft.TextButton("はい"),
                ft.TextButton("いいえ")
            ]
        )

        self.attentionDialog.actions[0].on_click = fun1
        self.attentionDialog.actions[1].on_click = fun2


class askSave:
    def __init__(self, fun1, fun2, fun3):
        self.askSaveDialog = ft.AlertDialog(
            title=ft.Text("comfirm"),
            modal=False,
            content=ft.Text("終了しますか？"),
            actions=[
                ft.TextButton("保存して終了する"),
                ft.TextButton("保存せず終了する"),
                ft.Text("キャンセル")
            ]
        )

        self.askSaveDialog.actions[0].on_click = fun1
        self.askSaveDialog.actions[1].on_click = fun2
        self.askSaveDialog.actions[2].on_click = fun3


class NotFolderSelected:
    def __init__(self, fun):
        self.banner = ft.Banner(
            bgcolor=ft.colors.AMBER_100,
            leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
            content=ft.Text(
                value="選択されたフォルダがありません:",
                color=ft.colors.BLACK,
            ),
            actions=[
                ft.TextButton(text="了解しました", style=ft.ButtonStyle(color=ft.colors.BLUE_600))
            ]
        )
        
        self.banner.actions[0].on_click = fun


class inputVideoNameDialog:
    def __init__(self, fun1, fun2):
        self.inputVideoNameDialog = ft.AlertDialog(
            title=ft.Text("新しい名前を入力してください"),
            modal=True,
            content=ft.TextField(),
            actions=[
                ft.TextButton("変更"),
                ft.TextButton("キャンセル")
            ]
        )

        self.inputVideoNameDialog.actions[0].on_click = fun1
        self.inputVideoNameDialog.actions[1].on_click = fun2