import flet as ft
from pathDatabase import pathDatabase
from dialogs import AttentionRemove

class removeList:
    def __init__(self, page: ft.Page):
        self.page = page
        self.refresh_data()
        self.instance_AR = AttentionRemove(
            lambda e: self.removeAndRefresh(),
            lambda e: self.page.close(self.instance_AR.attentionDialog)
        )

    def refresh_data(self):
        db = pathDatabase()
        self.folders = db.read_data()
        self.filerow = []
        self.checkboxes = []

        for folder in self.folders:
            checkbox = ft.Checkbox(label=f"{folder['Tag']}")
            self.checkboxes.append(checkbox)
            self.filerow.append(ft.DataRow(
                cells=[
                    ft.DataCell(checkbox),
                    ft.DataCell(ft.Text(f"{folder['FilePath']}")), 
                    ft.DataCell(ft.Text(f"{folder['CreatedAt']}"))
                ]
            ))

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
                    on_click=lambda e: self.page.open(self.instance_AR.attentionDialog)
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

    def removeAndRefresh(self):
        db = pathDatabase()
        for checkbox in self.checkboxes:
            if checkbox.value:
                db.remove_folder(checkbox.label)

        self.refresh_data()
        self.page.views.clear()
        self.page.views.append(self.makeView())
        self.page.update()

        self.page.close(self.instance_AR.attentionDialog)