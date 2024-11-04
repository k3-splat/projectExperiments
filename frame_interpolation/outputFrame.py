import cv2
import os

def save_frames_from_video(video_path, output_folder):
    # 出力フォルダが存在しない場合、作成する
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 動画ファイルを読み込む
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    # 動画が正常に読み込まれたか確認する
    if not cap.isOpened():
        print("動画を読み込めませんでした。ファイルパスを確認してください。")
        return

    while True:
        # フレームを1つ読み込む
        ret, frame = cap.read()

        # フレームが読み込めなかった場合（動画が終了した場合）はループを終了する
        if not ret:
            break

        # フレームを画像として保存する
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)

        print(f"フレーム {frame_count} を保存しました: {frame_filename}")

        frame_count += 1

    # 動画の読み込みを終了する
    cap.release()
    print("全てのフレームを保存しました。")

# 使用例
video_path = "./video/domo_running.mp4"      # 動画ファイルのパス
output_folder = "output_frames"     # フレーム画像を保存するフォルダ
save_frames_from_video(video_path, output_folder)