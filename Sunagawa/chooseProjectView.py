import flet as ft
from pathDatabase import pathDatabase
from projectRemoveView import removeList
from os import path

class projectList:
    def __init__(self, page: ft.Page):
        self.page = page
        self.constractRemove = removeList(self.page)

    def makeView(self):
        self.page.title = "プロジェクトを開く"
        backbutton = ft.IconButton(
            icon=ft.icons.ARROW_BACK, 
            on_click=lambda e: self.page.go("/startView"),
            tooltip="スタートに戻る"
        )
        appbar = ft.AppBar(
            leading=backbutton,
            title=ft.Text("続きを作るプロジェクトを選択してください"),
            actions=[
                ft.ElevatedButton(
                    icon=ft.icons.FILE_OPEN, 
                    text="開く",
                    on_click=lambda e: self.page.go("/mainView")
                )
            ]
        )
        datalabel = [
            ft.DataColumn(ft.Text("フォルダ名"), heading_row_alignment=ft.MainAxisAlignment.END),
            ft.DataColumn(ft.Text("フォルダパス")),
            ft.DataColumn(ft.Text("作成日時"))
        ]

        if not self.constractRemove.filerow:
            return ft.View("/projectOpenView", [
                appbar,
                ft.DataTable(
                    columns=datalabel
                ),
                ft.Text("作成されたプロジェクトがありません", theme_style=ft.TextThemeStyle.LABEL_LARGE)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        else:
            return ft.View("/projectOpenView", [
                appbar,
                ft.DataTable(
                    columns=datalabel,
                    rows=self.constractRemove.filerow
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)