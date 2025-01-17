import flet as ft
import os
import pickle
from flet import (
    Page,
    FilePickerResultEvent,
    Text
)
from pathDatabase import pathDatabase


class mkdir:
    def __init__(self):
        # 選択されたディレクトリのパス
        self.selected_directory = ""

    def input_directory_path(self, e: FilePickerResultEvent, page: ft.Page, dialog):
        # FilePickerからの選択結果を受け取り、パスを保存
        if e.path is None:
            return

        self.selected_directory = e.path
        page.open(dialog)

    def make_directory(self, folder_name: str):
        try:
            new_directory = os.path.join(self.selected_directory, folder_name)
            pd = pathDatabase()

            if os.path.exists(new_directory):
                raise FileExistsError()
            
            if pd.has_tag(folder_name):
                raise FileExistsError()

            os.mkdir(new_directory)
            return new_directory

        except FileExistsError:
            return -1
        
        except Exception:
            return -2
        

class saveAndloadFile:
    def __init__(self):
        self.saveAndloadPath = "C:/Users/gunda/projectExperiments/Sunagawa/pickles"

    def savefile(self, tag, obj):
        file = os.path.join(self.saveAndloadPath, tag + ".pickle")
        with open(file, 'wb') as f:
            pickle.dump(obj, f)

    def loadfile(self, tag):
        file = os.path.join(self.saveAndloadPath, tag + ".pickle")
        with open(file, "rb") as f:
            return pickle.loads(f)


class input_material:
    material_paths = []

    def __init__(self):
        self.path = ""

    def pick_files_result(self, e: FilePickerResultEvent):
        if e.files:
            self.path.value = ", ".join(file.path for file in e.files)
        else:
            self.path.value = "Cancelled!"

        input_material.material_paths.append(self.path.value)
        self.path.update()


class upload_movie:
    def __init__(self, page: Page):
        self.page = page
        constructor = mkdir(page)
        self.upload_files_lst = constructor.directory_paths

    def upload_files(self, e: FilePickerResultEvent):
        if self.upload_files_lst != None:
            for f in self.upload_files_lst:
                self.upload_files_lst.append(
                    ft.FilePickerUploadFile(
                        f.name,
                        upload_url=self.page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(self.upload_files_lst)
        else:
            emptydialog = emptyUploadList(self.page)
            self.page.open(emptydialog)