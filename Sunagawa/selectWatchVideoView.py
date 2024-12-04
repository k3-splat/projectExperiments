import flet as ft
import cv2
from os import path
from os import stat
from datetime import datetime
from pathDatabase import pathDatabase

class selectWatchVideo:
    video = ""

    def __init__(self, page: ft.Page):
        self.page = page
        self.output_thumnails = "C:/Users/gunda/projectExperiments/Sunagawa/thumnails"
        self.refresh_video()

    def refresh_video(self):
        db = pathDatabase()
        videos = db.get_video()
        self.filerow = []
        videoPaths = []
        videoTitles = []
        thumnailPaths = []

        for video in videos:
            videoPath = path.join(video['FilePath'], video['Title'])
            videoPaths.append(videoPath)

            videoTitle = video['Title']
            videoTitles.append(videoTitle)

            thumnailPath = path.join(self.output_thumnails, path.basename(video['FilePath']) + "_thumnail.png")
            thumnailPaths.append(thumnailPath)
            self.get_video_thumbnail(videoPath, thumnailPath)

        for pt, thumnail, title in zip(videoPaths, thumnailPaths, videoTitles):
            self.filerow.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Image(
                            src=thumnail,
                            width=120,
                            height=120,
                            fit=ft.ImageFit.COVER
                        )),
                        ft.DataCell(ft.Text(f"{title}")),
                        ft.DataCell(ft.Text(pt)), 
                        ft.DataCell(ft.Text(datetime.fromtimestamp(stat(pt).st_mtime))),
                        ft.DataCell(
                            ft.ElevatedButton(
                                icon=ft.icons.PLAY_CIRCLE, 
                                text="再生",
                                on_click=lambda e: self.openVideoView(pt)
                            )
                        )
                    ], selected=False
                )
            )
            print(pt)

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
        selectWatchVideo.video = video
        print(selectWatchVideo.video)
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
            ft.DataColumn(ft.Text(""))
        ]

        return ft.View("/selectWatchVideoView", [
            appbar,
            ft.DataTable(
                height=500,
                columns=datalabel,
                rows=self.filerow
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)


if __name__=="__main__":
    video = selectWatchVideo()