import flet as ft
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from os import path
from chooseProjectView import projectList
from pathDatabase import pathDatabase

class editVideoView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.db = pathDatabase()
        self.pick_file = ft.FilePicker(on_result=self.addAudio)
        self.page.overlay.append(self.pick_file)

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

    def addAudio(self, e:ft.FilePickerResultEvent):
        if not e.files or len(e.files) == 0:
            return
        
        video = VideoFileClip("C:/Users/gunda/projectExperiments/Sunagawa/test2/Flopping.mp4")
        # 効果音を読み込む
        sound_effect = AudioFileClip("C:/Users/gunda/Downloads/ラッパのファンファーレ.mp3")

        # 動画の音声を抽出
        original_audio = video.audio

        # 効果音を特定の時間に配置
        sound_effect = sound_effect.set_start(5.6)  # 5秒の時点で効果音を再生

        # 全ての音声トラックを合成
        final_audio = CompositeAudioClip([original_audio, sound_effect])

        # 音声を動画に適用
        final_video = video.set_audio(final_audio)

        # 最終的な動画を保存
        final_video.write_videofile("C:/Users/gunda/projectExperiments/Sunagawa/video_with_edited_audio.mp4")

        # 使用したクリップを閉じる
        video.close()
        sound_effect.close()
        final_video.close()

    def on_pan_update(self, e: ft.DragUpdateEvent):
        if e.control.left <= 751:
            e.control.left = max(0, e.control.left + e.delta_x)
        
        else:
            e.control.left = 750

        e.control.update()

    def makeView(self):
        # self.page.title = projectList.getprojectName()
        self.page.window.always_on_top = True
        self.page.spacing = 20
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # videoPath = self.db.get_video_from_tag(self.page.title)
        videoPath = "C:/Users/gunda/projectExperiments/Sunagawa/test2/Flopping.mp4"
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
        gd1 = ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.MOVE,
            drag_interval=10,
            left=0,
            top=0,
            on_horizontal_drag_update=self.on_pan_update,
            content=ft.Container(bgcolor=ft.colors.BLUE, width=50, height=50),
        )

        return ft.View("/editVideoView", [
            ft.AppBar(
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: self.page.go("/startView")),
                title=ft.Text(path.basename(videoPath))
            ),
            self.video,
            ft.Stack(
                controls=[gd1],
                alignment=ft.alignment.center,
                width=800,
                height=50
            ),
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
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)


if __name__=="__main__":
    pass