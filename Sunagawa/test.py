from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

# 動画ファイルを読み込む
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

print("音声編集と音響効果の適用が完了しました。")