import flet as ft
import os
from flet import (
    FilePickerResultEvent,
    Page,
    Text,
    AlertDialog,
)

class mkdir:
    directory_paths = []

    def __init__(self):
        self.selected_directory = ''

    def input_directory_path(self, page: Page, e: FilePickerResultEvent, dialog: AlertDialog):
        if e.path is None:
            return

        self.selected_directory = e.path
        page.open(dialog)
    
    def make_directory(self, page: Page, dialog: AlertDialog):
        self.selected_directory = self.selected_directory + '/' + dialog.content.value
        mkdir.directory_paths.append(self.selected_directory)
        os.mkdir(self.selected_directory)
        page.close(dialog)


class input_material:
    material_paths = []

    def __init__(self):
        self.path = Text()

    def pick_files_result(self, e: FilePickerResultEvent):
        if e.files:
            self.path.value = ", ".join(file.path for file in e.files)
        else:
            self.path.value = "Cancelled!"

        input_material.material_paths.append(self.path.value)
        self.path.update()

class upload_movie:
    def __init__(self, page):
        self.instance = mkdir(page)
        self.upload_files_lst = self.instance.directory_paths

    def upload_files(self, e: FilePickerResultEvent):
        if self.upload_files_lst != None:
            for f in self.upload_files_lst:
                upload_list.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(upload_list)

    choose_dlg = AlertDialog(
        title=Text("アップロードする動画を選択してください"),
        modal=True,
        content=[],
        actions=[]
    )