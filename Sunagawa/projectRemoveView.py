import flet as ft
import os
import shutil
from os import path
from pathDatabase import pathDatabase
from dialogs import AttentionRemove, inputVideoNameDialog

class removeList:
    def __init__(self, page: ft.Page):
        self.page = page
        self.refresh_data()
        self.instance_AR = AttentionRemove(
            lambda e: self.removeAndRefresh(),
            lambda e: self.page.close(self.instance_AR.attentionDialog)
        )
        self.instance_IV = inputVideoNameDialog(
            lambda e: self.changeTagName(self.instance_IV.inputVideoNameDialog.content.value),
            lambda e: self.page.close(self.instance_IV.inputVideoNameDialog)
        )

    def refresh_data(self):
        db = pathDatabase()
        self.folders = db.read_data()
        self.filerow = []

        for folder in self.folders:
            tag = folder['Tag']
            filepath = folder['FilePath']
            self.filerow.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"{tag}")),
                    ft.DataCell(ft.Text(f"{filepath}")), 
                    ft.DataCell(ft.Text(f"{folder['CreatedAt']}")),
                    ft.DataCell(
                        ft.PopupMenuButton(
                            content=ft.Icon(name=ft.icons.SETTINGS),
                            items=[
                                ft.PopupMenuItem(
                                    icon=ft.icons.FOLDER,
                                    text="名前を変更する",
                                    on_click=lambda e, tg=tag: self.openTagNameDialog(tg)
                                ),
                                ft.PopupMenuItem(
                                    icon=ft.icons.DELETE,
                                    text="削除する",
                                    on_click=lambda e, tg=tag: self.setRemoveFilePath(tg)
                                ),
                            ],
                            tooltip="管理する"
                        )
                    )
                ]
            ))

    def makeView(self):
        self.page.title = "プロジェクトを管理する"
        backbutton = ft.IconButton(
            icon=ft.icons.ARROW_BACK, 
            on_click=lambda e: self.page.go("/startView"),
            tooltip="スタートに戻る"
        )
        appbar = ft.AppBar(
            leading=backbutton,
            title=ft.Text("プロジェクトを管理する")
        )
        datalabel = [
            ft.DataColumn(ft.Text("フォルダ名")),
            ft.DataColumn(ft.Text("フォルダパス")),
            ft.DataColumn(ft.Text("作成日時")),
            ft.DataColumn(ft.Text("操作"))
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
        
    def openTagNameDialog(self, tag):
        self.tag = tag
        self.page.open(self.instance_IV.inputVideoNameDialog)

    def changeTagName(self, newTag):
        pd = pathDatabase()
        pd.update_tag(self.tag, newTag)

        self.refresh_data()
        self.page.close(self.instance_IV.inputVideoNameDialog)
        self.page.views.clear()
        self.page.views.append(self.makeView())
        self.page.update()

    def setRemoveFilePath(self, tag):
        self.tag = tag
        self.page.open(self.instance_AR.attentionDialog)

    def removeAndRefresh(self):
        pd = pathDatabase()

        if path.exists(self.tag):
            pd.remove_folder(self.tag)

        self.refresh_data()
        self.page.views.clear()
        self.page.views.append(self.makeView())
        self.page.update()

        self.page.close(self.instance_AR.attentionDialog)