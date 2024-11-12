import flet as ft
import os
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    TextField,
    icons,
    AlertDialog,
    TextButton,
    CrossAxisAlignment
)

class mkdir:
    directory_paths = []

    mkdir_dlg = AlertDialog(
        title=Text("フォルダ名を入力してください"),
        modal=True,
        content=TextField(),
        actions=[
            TextButton("作成", on_click=lambda e: None), #ダミーだから，インスタンスを作ったときに実際の処理を書く
            TextButton("キャンセル", on_click=lambda e: None)
        ]
    )

    def __init__(self, page):
        self.page = page
        self.selected_directory = ''

    def get_directory_path(self, e: FilePickerResultEvent):
        if e.path is None:
            return

        self.selected_directory = e.path
        self.page.open(self.mkdir_dlg)
    
    def make_directory(self, page: Page, e: FilePickerResultEvent):
        self.selected_directory = self.selected_directory + '/' + mkdir.mkdir_dlg.content.value
        mkdir.directory_paths.append(self.selected_directory)
        os.mkdir(self.selected_directory)
        page.close(mkdir.mkdir_dlg)


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

def main(page: Page):
    make_directory = mkdir(page)
    get_directory_dialog = FilePicker(on_result=make_directory.get_directory_path)

    mkdir.mkdir_dlg.actions[0].on_click = make_directory.make_directory #コンストラクタ作成後にダイアログの機能を与える
    mkdir.mkdir_dlg.actions[1].on_click = lambda e: page.close(mkdir.mkdir_dlg)

    pick_material = input_material()
    pick_material_dialog = FilePicker(on_result=pick_material.pick_files_result)

    page.title = "ファイルのやり取り"
    page.horizontal_alignment = CrossAxisAlignment.CENTER

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
                ElevatedButton(
                    "Pick files",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_material_dialog.pick_files(
                        allow_multiple=True,
                        allowed_extensions=["jpg", "png", "wav", "mp3"]
                    ),
                ),
                pick_material.path,
            ]
        )
    )

if __name__ == "__main__":
    ft.app(target=main)