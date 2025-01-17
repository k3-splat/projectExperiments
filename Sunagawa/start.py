import flet as ft
from datetime import datetime
import fileLoad as fl
import dialogs as dl
import pathDatabase as pd
from chooseProjectView import projectList
import asyncio
from os import path

class startView:
    def __init__(self, page: ft.Page):
        self.page = page
        pdInstance = pd.pathDatabase()
        pdInstance.initialize_csv()

        self.make_directory = fl.mkdir()
        selectDirectory = ft.FilePicker(on_result=lambda e: self.make_directory.input_directory_path(e, self.page, self.inputfoldernamedialog.inputFolderNameDialog))
        self.inputfoldernamedialog = dl.inputFolderNameDialog(
            lambda e: self.mkdir_hole(),
            lambda e: self.page.close(self.inputfoldernamedialog.inputFolderNameDialog)
        )
        choosecontinewdialog = dl.chooseContiNewDialog(
            lambda e: self.page.close(choosecontinewdialog.bottom_sheet),
            lambda e: selectDirectory.get_directory_path(dialog_title="パスを選択"),
            lambda e: self.page.go("/projectOpenView")
        )
        choosewatchvideo = dl.chooseWatchVideo(
            lambda e: self.page.close(choosewatchvideo.bottom_sheet),
            lambda e: self.page.go("/selectWatchVideoView"),
            lambda e: self.page.open(self.browserdialog.minnanoDialog)
        )
        self.choosemanagedialog = dl.manageFolders(
            lambda e: self.page.close(self.choosemanagedialog.bottom_sheet),
            lambda e: self.page.go("/removeView"),
            lambda e: self.page.go("/manageVideoView")
        )
        self.browserdialog = dl.minnanoDialog(
            lambda e: self.page.close(self.browserdialog.minnanoDialog)
        )

        self.page.title = "スタート"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.page.overlay.extend([selectDirectory])

        self.time_text = ft.Text(
            value="",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.ORANGE_800
        )
        asyncio.create_task(self.update_time())

        self.img_title = ft.Image(
            src="/title_kari.png",
            width=760,
            height=100,
            fit=ft.ImageFit.CONTAIN,
        )

        img_miru = ft.Image(
            src="/mirubotan.png",
            width=250,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        )

        self.img_miru_clickable = ft.GestureDetector(
            content=img_miru,
            on_tap=lambda e: page.open(choosewatchvideo.bottom_sheet),
            mouse_cursor=ft.MouseCursor.CLICK
        )

        img_tsukuru = ft.Image(
            src="/tsukurubotan.png",
            width=250,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        )

        self.img_tsukuru_clickable = ft.GestureDetector(
            content=img_tsukuru,
            on_tap=lambda e: self.page.open(choosecontinewdialog.bottom_sheet),
            disabled=self.page.web,
            mouse_cursor=ft.MouseCursor.CLICK
        )

        img_kanri = ft.Image(
            src="/kanribotan.png", width=250,
            height=200,
            fit=ft.ImageFit.CONTAIN
        )

        self.img_kanri_clickable = ft.GestureDetector(
            content=img_kanri,
            on_tap=lambda e: self.page.open(self.choosemanagedialog.bottom_sheet),
            disabled=self.page.web,
            mouse_cursor=ft.MouseCursor.CLICK
        )

    def mkdir_hole(self):
        filePath = self.make_directory.make_directory(self.inputfoldernamedialog.inputFolderNameDialog.content.value)

        if filePath == -1:
            self.inputfoldernamedialog.inputFolderNameDialog.content.label = "This name is already used!"
            self.inputfoldernamedialog.inputFolderNameDialog.content.border_color = 'RED'
        elif filePath == -2:
            self.inputfoldernamedialog.inputFolderNameDialog.content.label = "Making directory is failure. Please try it again."
            self.inputfoldernamedialog.inputFolderNameDialog.content.border_color = 'RED'
        else:
            projectList.setprojectName(path.basename(filePath))

            self.inputfoldernamedialog.inputFolderNameDialog.content.label = ""
            self.inputfoldernamedialog.inputFolderNameDialog.content.border_color = ''
            self.inputfoldernamedialog.inputFolderNameDialog.content.value = ""
            self.inputfoldernamedialog.inputFolderNameDialog.content.update()

            db = pd.pathDatabase()
            db.add_folder(filePath)
            self.page.go("/mainView")

    async def update_time(self):
        while True:
            try:
                current_time = datetime.now().strftime("%Y/%m/%d         %H:%M:%S")
                self.time_text.value = current_time
                self.page.update()
                await asyncio.sleep(1)
            except Exception as e:
                print(f"Error updating time: {e}")
                break

    def startView(self):
        self.page.title = "スタート"
        return ft.View("/startView", [
            ft.Row(
                [self.img_title],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.Container(  # 時刻
                        content=self.time_text,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.WHITE,
                        width=400,
                        height=50,
                        border_radius=5,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    self.img_miru_clickable,
                    self.img_kanri_clickable,
                    self.img_tsukuru_clickable,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ], bgcolor="WHITE", vertical_alignment=ft.MainAxisAlignment.CENTER)