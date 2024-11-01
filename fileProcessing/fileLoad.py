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
    directory_paths = []

    def __init__(self, page):
        self.page = page
        self.selected_directory = ''

    def get_directory_path(self, e: FilePickerResultEvent):
        self.selected_directory = e.path
        self.page.open(mkdir.mkdir_dlg)
    
    def make_directory(self, e):
        self.selected_directory = self.selected_directory + '/' + mkdir.mkdir_dlg.content.value
        mkdir.directory_paths.append(self.selected_directory)
        os.mkdir(self.selected_directory)
        self.page.close(mkdir.mkdir_dlg)

    mkdir_dlg = ft.AlertDialog(
        title=ft.Text("フォルダ名を入力してください"),
        modal=True,
        content=ft.TextField(),
        actions=[
            ft.TextButton("作成", on_click=lambda e: None), #ダミーだから，インスタンスを作ったときに実際の処理を書く
            ft.TextButton("キャンセル", on_click=lambda e: None)
        ]
    )

class input_material:
    material_paths = []

    def __init__(self, page):
        self.page = page
        self.path = Text()

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            self.path.value = ", ".join(file.path for file in e.files)
        else:
            self.path.value = "Cancelled!"

        input_material.material_paths.append(self.path.value)
        self.path.update()

def main(page: Page):
    make_directory = mkdir(page)
    get_directory_dialog = FilePicker(on_result=make_directory.get_directory_path)

    mkdir.mkdir_dlg.actions[0].on_click = make_directory.make_directory
    mkdir.mkdir_dlg.actions[1].on_click = lambda e: page.close(mkdir.mkdir_dlg)

    pick_material = input_material(page)
    pick_material_dialog = FilePicker(on_result=pick_material.pick_files_result)

    page.title = "ファイルのやり取り"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.overlay.extend([get_directory_dialog, pick_material_dialog])

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
        Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_material_dialog.pick_files(
                        allow_multiple=True,
                        allowed_extensions=["jpg", "png", "wav", "mp3"]
                    ),
                ),
                pick_material.path,
            ]
        )
    )


ft.app(target=main)