import flet as ft
import cv2
import os
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)

class mkdir:
    directory_name = []

    def __init__(self, page):  # pageをコンストラクタに渡す
        self.page = page
        self.selected_directory = ""

    def get_directory_path(self, e: FilePickerResultEvent):
        self.selected_directory = e.path
        self.page.open(mkdir.mkdir_dlg)
    
    def make_directory(self, e):
        self.selected_directory += mkdir.mkdir_dlg.content.value
        mkdir.directory_name.append(self.selected_directory)
        os.mkdir(self.selected_directory)
        self.page.close(mkdir.mkdir_dlg)

    mkdir_dlg = ft.AlertDialog(
        title=ft.Text("フォルダ名を入力してください"),
        modal=True,
        content=ft.TextField(),
        actions=[
            ft.TextButton("作成", on_click=lambda e: None),
            ft.TextButton("キャンセル", on_click=lambda e: None)
        ]
    )
    

def main(page: Page):
    make_directory = mkdir(page)
    get_directory_dialog = FilePicker(on_result=make_directory.get_directory_path)

    mkdir.mkdir_dlg.actions[0].on_click = make_directory.make_directory
    mkdir.mkdir_dlg.actions[1].on_click = lambda e: page.close(mkdir.mkdir_dlg)

    page.title = "AlertDialog examples"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.overlay.extend([get_directory_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    "新規ファイルを作成",
                    icon=icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(dialog_title="フォルダーを選択"),
                    disabled=page.web,
                ),
            ]
        ),
    )


ft.app(target=main)