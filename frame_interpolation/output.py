import cv2
import os

def create_video_from_frames(input_folder, output_video_path, fps):
    # フレーム画像が保存されているディレクトリ内のファイル一覧を取得
    images = [img for img in os.listdir(input_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    images.sort()  # フレーム順になるようにソート（例えば、名前が「frame1.png」「frame2.png」などの場合）

    # 画像から動画のフレームサイズを決定
    if not images:
        print("画像ファイルが見つかりません")
        return
    
    first_frame = cv2.imread(os.path.join(input_folder, images[0]))
    height, width, layers = first_frame.shape
    frame_size = (width, height)

    # 動画の書き込みオブジェクトを作成
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4形式で保存する
    out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

    # 画像を順番に読み込み、動画に書き込む
    for image in images:
        img_path = os.path.join(input_folder, image)
        frame = cv2.imread(img_path)
        out.write(frame)

    # リソースを解放
    out.release()
    print(f"動画ファイルが作成されました: {output_video_path}")

# 使用例
input_folder = "./interpolation_frame"  # 画像ファイルが保存されているフォルダへのパス
output_video_path = "./output_video_interpolation.mp4"  # 出力する動画ファイルのパス
fps = 24  # 動画のFPS（フレーム毎秒）

create_video_from_frames(input_folder, output_video_path, fps)