import flet as ft
import cv2
from os import path
import pathlib
from pathDatabase import pathDatabase

class selectWatchVideo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.output_thumnails = "C:/Users/gunda/projectExperiments/Sunagawa/thumnails"
        self.refresh_video()

        self.thumnails = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
        )

    def refresh_video(self):
        db = pathDatabase()
        videos = db.get_video()

        for video in videos:
            input_path = path.join(video['FilePath'], video['Title'])
            output_path = path.join(self.output_thumnails, path.basename(video['FilePath']) + "_thumnail.png")
            self.get_video_thumbnail(input_path, output_path)

    def get_video_thumbnail(self, video_path, output_path):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError("動画を開くことができませんでした。パスを確認してください。")

        # 最初のフレームを取得
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 最初のフレームに設定
        ret, frame = cap.read()

        if not ret:
            raise ValueError("最初のフレームを取得できませんでした。")

        # サムネイルを保存する場合
        if output_path:
            cv2.imwrite(output_path, frame)

        # リソースを解放
        cap.release()

    def makeView(self):
        self.refresh_video()
        self.page.title = "動画を見る"
        backbutton = ft.IconButton(
            icon=ft.icons.ARROW_BACK, 
            on_click=lambda e: self.page.go("/startView"),
            tooltip="スタートに戻る"
        )
        appbar = ft.AppBar(
            leading=backbutton,
            title=ft.Text("見たい動画を選択してください")
        )

        input_list = list(pathlib.Path(self.output_thumnails).glob('*.png'))
        for thumnail in input_list:
            self.thumnails.controls.append(
                ft.CupertinoContextMenu(
                    enable_haptic_feedback=True,
                    content=ft.Image(
                        src=thumnail,
                        fit=ft.ImageFit.NONE,
                        repeat=ft.ImageRepeat.NO_REPEAT,
                        border_radius=ft.border_radius.all(10)
                    ),
                    actions=[
                        ft.CupertinoContextMenuAction(
                            text="Action 1",
                            is_default_action=True,
                            trailing_icon=ft.icons.CHECK,
                            on_click=lambda e: print("Action 1"),
                        ),
                        ft.CupertinoContextMenuAction(
                            text="Action 2",
                            trailing_icon=ft.icons.MORE,
                            on_click=lambda e: print("Action 2"),
                        ),
                        ft.CupertinoContextMenuAction(
                            text="Action 3",
                            is_destructive_action=True,
                            trailing_icon=ft.icons.CANCEL,
                            on_click=lambda e: print("Action 3"),
                        )
                    ]
                )
            )

        return ft.View("/selectWatchVideoView", [
            appbar,
            self.thumnails
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)


if __name__=="__main__":
    video = selectWatchVideo()        