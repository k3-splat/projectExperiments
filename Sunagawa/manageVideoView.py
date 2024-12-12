import flet as ft
import cv2
import os
from os import path
from os import stat
from datetime import datetime
from pathDatabase import pathDatabase
from dialogs import AttentionRemove

class manageVideo:
    removeVideo = ""

    @classmethod
    def setremoveVideo(cls, value):
        cls.removeVideo = value

    @classmethod
    def getremoveVideo(cls):
        return cls.removeVideo

    def __init__(self, page: ft.Page):
        self.page = page
        self.output_thumnails = "C:/Users/gunda/projectExperiments/Sunagawa/thumnails"
        self.instance_AR = AttentionRemove(
            lambda e: self.removeAndrefresh(),
            lambda e: self.page.close(self.instance_AR.attentionDialog)
        )

        self.refresh_video()

    def refresh_video(self):
        db = pathDatabase()
        videos = db.get_video()
        self.filerow = []
        self.refreshThumnails()

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
                            ft.PopupMenuButton(
                                content=ft.Icon(name=ft.icons.VIDEO_SETTINGS),
                                items=[
                                    ft.PopupMenuItem(icon=ft.icons.FILE_UPLOAD, text="投稿する", on_click=lambda e: None),
                                    ft.PopupMenuItem(
                                        icon=ft.icons.DELETE,
                                        text="削除する",
                                        on_click=lambda e, vp=videoPath: self.setremovevideoAndopen(vp)
                                    ),
                                ],
                                tooltip="管理する"
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

    def setremovevideoAndopen(self, videopath):
        manageVideo.setremoveVideo(videopath)
        self.page.open(self.instance_AR.attentionDialog)

    def removeAndrefresh(self):
        if path.exists(manageVideo.removeVideo):
            os.remove(manageVideo.removeVideo)
        
        self.refresh_video()
        self.page.close(self.instance_AR.attentionDialog)
        self.page.views.clear()
        self.page.views.append(self.makeView())
        self.page.update()

    def refreshThumnails(self):
        for _, _, thumnails in os.walk(self.output_thumnails):
            for thumnail in thumnails:
                tp = path.join(self.output_thumnails, thumnail)
                os.remove(tp)

    def makeView(self):
        self.refresh_video()
        self.page.title = "動画を管理する"
        backbutton = ft.IconButton(
            icon=ft.icons.ARROW_BACK, 
            on_click=lambda e: self.page.go("/startView"),
            tooltip="スタートに戻る"
        )
        appbar = ft.AppBar(
            leading=backbutton,
            title=ft.Text("管理する動画を選択してください")
        )
        datalabel = [
            ft.DataColumn(ft.Text("サムネイル画像")),
            ft.DataColumn(ft.Text("動画タイトル")),
            ft.DataColumn(ft.Text("動画パス")),
            ft.DataColumn(ft.Text("作成日時")),
            ft.DataColumn(ft.Text("操作"))
        ]

        if not self.filerow:
            return ft.View("/manageVideoView", [
                appbar,
                ft.DataTable(
                    columns=datalabel
                ),
                ft.Text("作成された動画がありません", theme_style=ft.TextThemeStyle.LABEL_LARGE)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        else:
            return ft.View("/manageVideoView", [
                appbar,
                ft.DataTable(
                    height=500,
                    columns=datalabel,
                    rows=self.filerow
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)


if __name__=="__main__":
    pass