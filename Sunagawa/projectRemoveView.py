import flet as ft
from pathDatabase import pathDatabase
from os import path

class removeList:
    def __init__(self, page: ft.Page):
        self.page = page
        self.refresh_data()

    def refresh_data(self):
        db = pathDatabase()
        n = 1
        self.filerow = []
        self.checkList = []
        while True:
            pathInfo = db.get_nth_entry(n)
            if pathInfo == -1:
                print("ファイル読み込みエラーです")
                break
            elif pathInfo == -2:
                break
            else:
                if path.exists(pathInfo['FilePath']):
                    checkbox = ft.Checkbox(label=f"{pathInfo['Tag']}")
                    self.checkList.append(checkbox)
                    self.filerow.append(ft.DataRow(
                        cells=[
                            ft.DataCell(checkbox),
                            ft.DataCell(ft.Text(f"{pathInfo['FilePath']}")), 
                            ft.DataCell(ft.Text(f"{pathInfo['CreatedAt']}"))
                        ]
                    ))
                else:
                    db.remove_folder(pathInfo['Tag'])

                n += 1

    def makeView(self):
        self.page.title = "プロジェクトを削除する"
        backbutton = ft.IconButton(
            icon=ft.icons.ARROW_BACK, 
            on_click=lambda e: self.page.go("/startView"),
            tooltip="スタートに戻る"
        )
        appbar = ft.AppBar(
            leading=backbutton,
            title=ft.Text("削除するプロジェクトを選択"),
            actions=[
                ft.ElevatedButton(
                    icon=ft.icons.DELETE, 
                    text="削除する", 
                    on_click=self.removeAndRefresh
                )
            ]
        )
        datalabel = [
            ft.DataColumn(ft.Text("フォルダ名"), heading_row_alignment=ft.MainAxisAlignment.END),
            ft.DataColumn(ft.Text("フォルダパス")),
            ft.DataColumn(ft.Text("作成日時"))
        ]

        if not self.filerow:
            return ft.View("/removeView", [
                appbar,
                ft.DataTable(
                    columns=datalabel
                ),
                ft.Text("作成されたプロジェクトがありません", theme_style=ft.TextThemeStyle.LABEL_LARGE)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        else:
            return ft.View("/removeView", [
                appbar,
                ft.DataTable(
                    columns=datalabel,
                    rows=self.filerow
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def removeAndRefresh(self, e=None):
        db = pathDatabase()
        for checkbox in self.checkList:
            if checkbox.value:
                db.remove_folder(checkbox.label)

        self.refresh_data()
        self.page.views.clear()
        self.page.views.append(self.makeView())
        self.page.update()