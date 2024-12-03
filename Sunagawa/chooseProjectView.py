import flet as ft
from pathDatabase import pathDatabase
from os import path

class projectList:
    projectName = "hoge"

    def __init__(self, page: ft.Page):
        self.page = page
        self.refresh_data()

    def refresh_data(self):
        db = pathDatabase()
        self.folders = db.read_data()
        self.filerow = []
        self.checkboxes = []

        for folder in self.folders:
            checkbox = ft.Checkbox(label=f"{folder['Tag']}", on_change=self.checkbox_changed)
            self.checkboxes.append(checkbox)
            self.filerow.append(ft.DataRow(
                cells=[
                    ft.DataCell(checkbox),
                    ft.DataCell(ft.Text(f"{folder['FilePath']}")), 
                    ft.DataCell(ft.Text(f"{folder['CreatedAt']}"))
                ]
            ))


    def checkbox_changed(self, e):
        for checkbox in self.checkboxes:
            if checkbox != e.control:
                checkbox.value = False

        self.page.update()

    def returnName(self):
        return projectList.projectName
    
    def openProject(self):
        for checkbox in self.checkboxes:
            if checkbox.value:
                projectList.projectName = f"{checkbox.label}"
                print(projectList.projectName)
                break

        self.page.update()
        self.page.go("/mainView")

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
                    on_click=lambda e: self.openProject()
                )
            ]
        )
        datalabel = [
            ft.DataColumn(ft.Text("フォルダ名"), heading_row_alignment=ft.MainAxisAlignment.END),
            ft.DataColumn(ft.Text("フォルダパス")),
            ft.DataColumn(ft.Text("作成日時"))
        ]

        if not self.filerow:
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
                    rows=self.filerow
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)