import flet as ft
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from os import path
from chooseProjectView import projectList
from pathDatabase import pathDatabase
from dialogs import inputTimingDialog

class editVideoView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.projectname = projectList.getprojectName()
        self.db = pathDatabase()
        self.pick_file = ft.FilePicker(on_result=self.getaudiopath)
        self.page.overlay.append(self.pick_file)
        self.inputdialog = inputTimingDialog(
            lambda e: self.addAudio(self.inputdialog.inputTimingDialog.content.value),
            lambda e: self.page.close(self.inputdialog.inputTimingDialog)
        )

    def handle_pause(self, e):
        self.video.pause()
        print("Video.pause()")

    def handle_play(self, e):
        self.video.play()
        print("Video.play()")

    def handle_stop(self, e):
        self.video.stop()
        print("Video.stop()")

    def handle_playback_rate_change(self, e):
        self.video.playback_rate = e.control.value
        self.page.update()
        print(f"Video.playback_rate = {e.control.value}")

    def getaudiopath(self, e:ft.FilePickerResultEvent):
        if not e.files or len(e.files) == 0:
            return

        # 効果音を読み込む
        self.audiopath = e.files[0].path
        self.page.open(self.inputdialog.inputTimingDialog)

    def addAudio(self, timing):
        int_timing = int(timing) 
        if 0 > int_timing or self.clip.duration <= int_timing:
            self.page.close(self.inputdialog.inputTimingDialog)
            return
        
        self.output_path = path.join(self.db.get_path_from_tag(self.projectname), self.db.get_title_from_tag(self.projectname))

        sound_effect = AudioFileClip(self.audiopath)
        self.audiolist.append(self.audiopath)

        # 効果音を特定の時間に配置
        sound_effect = sound_effect.set_start(int_timing)  # 5秒の時点で効果音を再生

        # 全ての音声トラックを合成
        final_audio = CompositeAudioClip([sound_effect])

        # 音声を動画に適用
        final_video = self.clip.set_audio(final_audio)

        # 最終的な動画を保存
        final_video.write_videofile(self.output_path)

        # 使用したクリップを閉じる
        self.clip.close()
        sound_effect.close()
        final_video.close()

        self.page.close(self.inputdialog.inputTimingDialog)

    def makeView(self):
        self.page.title = self.projectname
        self.page.window.always_on_top = True
        self.page.spacing = 20
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        videoPath = self.db.get_video_from_tag(self.page.title)
        self.clip = VideoFileClip(videoPath)
        self.video = ft.Video(
            expand=True,
            playlist = [ft.VideoMedia(videoPath)],
            fill_color=ft.colors.BLUE_400,
            aspect_ratio=16/9,
            volume=100,
            autoplay=False,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False
        )
        self.audiolist = []

        return ft.View("/editVideoView", [
            ft.AppBar(
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: self.page.go("/mainView")),
                title=ft.Text(path.basename(videoPath))
            ),
            self.video,
            ft.Row(
                wrap=True,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.ElevatedButton("再生", on_click=self.handle_play),
                    ft.ElevatedButton("停止", on_click=self.handle_pause),
                    ft.ElevatedButton("先頭へ戻る", on_click=self.handle_stop),
                    ft.ElevatedButton("音声の追加", on_click=lambda e: self.pick_file.pick_files(dialog_title="音声ファイルを選択", allowed_extensions=["mp3", "wav"]))
                ],
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, vertical_alignment=ft.MainAxisAlignment.CENTER)


if __name__=="__main__":
    pass