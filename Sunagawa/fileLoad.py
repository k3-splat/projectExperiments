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