import flet as ft
from datetime import datetime
import fileLoad as fl
import dialogs as dl
import asyncio

class startView:
    def __init__(self, page: ft.Page):
        self.page = page

        self.make_directory = fl.mkdir()
        selectDirectory = ft.FilePicker(on_result=lambda e: self.make_directory.input_directory_path(e, page, self.inputfoldernamedialog.inputFolderNameDialog))
        self.inputfoldernamedialog = dl.inputFolderNameDialog(
            lambda e: startView.mkdir_hole(self),
            lambda e: startView.dialogCloseAndResetDialog(self, self.inputfoldernamedialog.inputFolderNameDialog)
        )
        choosecontinewdialog = dl.chooseContiNewDialog(
            lambda e: page.close(choosecontinewdialog.bottom_sheet),
            lambda e: selectDirectory.get_directory_path(dialog_title="パスを選択"),
            lambda e: None
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
            src=f"/titlekamo.png",
            width=760,
            height=100,
            fit=ft.ImageFit.CONTAIN,
        )

        img_miru = ft.Image(
            src=f"/mirubotan.png",
            width=250,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        )

        self.img_miru_clickable = ft.GestureDetector(
            content=img_miru,
            on_tap=lambda e: None,
            mouse_cursor=ft.MouseCursor.CLICK
        )

        img_tsukuru = ft.Image(
            src=f"/tsukurubotan.png",
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

    def mkdir_hole(self):
        successOrNot = self.make_directory.make_directory(self.inputfoldernamedialog.inputFolderNameDialog.content.value)

        if successOrNot == -1:
            self.inputfoldernamedialog.inputFolderNameDialog.content.label = "This name is already used!"
            self.inputfoldernamedialog.inputFolderNameDialog.content.border_color = 'RED'
        elif successOrNot == -2:
            self.inputfoldernamedialog.inputFolderNameDialog.content.label = "Making directory is failure. Please try it again."
            self.inputfoldernamedialog.inputFolderNameDialog.content.border_color = 'RED'
        else:
            self.inputfoldernamedialog.inputFolderNameDialog.content.label = ""
            self.inputfoldernamedialog.inputFolderNameDialog.content.border_color = ''
            self.inputfoldernamedialog.inputFolderNameDialog.content.value = ""
            self.inputfoldernamedialog.inputFolderNameDialog.content.update()

    def dialogCloseAndResetDialog(self, dialog):
        self.page.close(dialog)
        self.inputfoldernamedialog.inputFolderNameDialog.content.label = ""
        self.inputfoldernamedialog.inputFolderNameDialog.content.border_color = ''
        self.inputfoldernamedialog.inputFolderNameDialog.content.value = ""
        self.inputfoldernamedialog.inputFolderNameDialog.content.update()

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
                    ft.Container(
                        content=ft.Text("絵"),
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.BLACK,
                        width=200,
                        height=200,
                        border_radius=5,
                    ),
                    self.img_tsukuru_clickable,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text("取扱説明書"),
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.ORANGE_800,
                        width=300,
                        height=50,
                        border_radius=5,
                        ink=True,
                        on_click=lambda e: self.page.go("/MainPage"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ], bgcolor="WHITE")

    
    def create_view2(self):
        self.page.title = "view2"

        return ft.View("/view2", [
            ft.AppBar(title=ft.Text("view2"),
                      bgcolor=ft.colors.RED),
            ft.TextField(value="view2"),
            ft.ElevatedButton(
                "Go to view1", on_click=lambda _: self.page.go("/startView")),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text("絵"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.BLACK,
                        width=200,
                        height=200,
                        border_radius=5,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ])