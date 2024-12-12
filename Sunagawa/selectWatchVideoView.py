import flet as ft
import cv2
from os import path
from os import stat
from datetime import datetime
from pathDatabase import pathDatabase

class selectWatchVideo:
    video = ""

    @classmethod
    def setVideo(cls, value):
        cls.video = value

    @classmethod
    def getVideo(cls):
        return cls.video

    def __init__(self, page: ft.Page):
        self.page = page
        self.output_thumnails = "/thumnails"
        self.refresh_video()

    def refresh_video(self):
        db = pathDatabase()
        videos = db.get_video()
        self.filerow = []

        for video in videos:
            videoPath = path.join(video['FilePath'], video['Title'])
            videoTitle = video['Title']
            thumnailPath = path.join(self.output_thumnails, path.basename(video['FilePath']) + "_thumnail.png")
            self.get_video_thumbnail(videoPath, thumnailPath)

            self.filerow.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Image(
                            src=thumnailPath,
                            width=120,
                            height=120,
                            fit=ft.ImageFit.COVER
                        )),
                        ft.DataCell(ft.Text(videoTitle)),
                        ft.DataCell(ft.Text(videoPath)), 
                        ft.DataCell(ft.Text(datetime.fromtimestamp(stat(videoPath).st_mtime))),
                        ft.DataCell(
                            ft.ElevatedButton(
                                icon=ft.icons.PLAY_CIRCLE, 
                                text="再生",
                                on_click=lambda e, vp=videoPath: self.openVideoView(vp)
                            )
                        )
                    ], selected=False
                )
            )

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

    def openVideoView(self, video):
        selectWatchVideo.setVideo(video)
        self.page.go("/videoPlayView")

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
        datalabel = [
            ft.DataColumn(ft.Text("サムネイル画像")),
            ft.DataColumn(ft.Text("動画タイトル")),
            ft.DataColumn(ft.Text("動画パス")),
            ft.DataColumn(ft.Text("作成日時")),
            ft.DataColumn(ft.Text("操作"))
        ]

        if not self.filerow:
            return ft.View("/selectWatchVideoView", [
                appbar,
                ft.DataTable(
                    columns=datalabel
                ),
                ft.Text("作成された動画がありません", theme_style=ft.TextThemeStyle.LABEL_LARGE)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        else:
            return ft.View("/selectWatchVideoView", [
                appbar,
                ft.DataTable(
                    height=500,
                    columns=datalabel,
                    rows=self.filerow
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)


if __name__=="__main__":
    selectWatchVideo.setVideo("hoge")