import cv2
import numpy as np
import os

def optical_flow_interpolation(prev_frame_path, next_frame_path, alpha=0.5, output_path="color_interpolated_frame.png"):
    # 前フレームと後フレームの読み込み（カラー画像）
    prev_frame = cv2.imread(prev_frame_path)
    next_frame = cv2.imread(next_frame_path)
    
    # 画像が正しく読み込まれているか確認
    if prev_frame is None or next_frame is None:
        raise ValueError("フレームが正しく読み込まれていません。ファイルパスを確認してください。")
    
    # 各チャンネル（B, G, R）に分けて処理
    channels = cv2.split(prev_frame)
    next_channels = cv2.split(next_frame)
    interpolated_channels = []

    for i in range(3):  # 各チャンネル (B, G, R) について
        # オプティカルフローの計算（グレースケール画像として扱う）
        flow = cv2.calcOpticalFlowFarneback(channels[i], next_channels[i], None, 0.5, 3, 15, 3, 5, 1.2, 0)

        # オプティカルフローの移動ベクトルに基づいたピクセルの補間
        h, w = channels[i].shape
        flow_x, flow_y = flow[..., 0] * alpha, flow[..., 1] * alpha

        # マッピングを計算して、リマップによりピクセルを移動
        map_x, map_y = np.meshgrid(np.arange(w), np.arange(h))
        map_x = (map_x + flow_x).astype(np.float32)
        map_y = (map_y + flow_y).astype(np.float32)
        
        # シフトしたピクセルの位置での補間
        interpolated_channel = cv2.remap(channels[i], map_x, map_y, interpolation=cv2.INTER_LINEAR)

        # 前後フレームをアルファブレンディング
        blended_channel = cv2.addWeighted(interpolated_channel, 1 - alpha, next_channels[i], alpha, 0)
        
        interpolated_channels.append(blended_channel)

    # 各チャンネルを統合してカラー画像に
    color_interpolated_frame = cv2.merge(interpolated_channels)

    # 画像を保存または表示
    cv2.imwrite(output_path, color_interpolated_frame)
    print(f"Interpolated frame saved as {output_path}")

def process_frames_in_directory(directory, alpha=0.5):
    # ディレクトリ内のファイル名を取得し、ソート
    frame_files = sorted([f for f in os.listdir(directory) if f.endswith(".png")])
    
    # 奇数番のファイルのみ選択し、ペアリングして関数を適用
    for i in range(1, len(frame_files) - 1, 2):  # 奇数インデックスを指定
        prev_frame_path = os.path.join(directory, frame_files[i])
        next_frame_path = os.path.join(directory, frame_files[i + 2])
        
        # 出力ファイル名を生成
        output_filename = f"interpolated_{i:04d}_{i+2:04d}.png"
        output_path = os.path.join(directory, output_filename)
        
        # 関数を適用
        optical_flow_interpolation(prev_frame_path, next_frame_path, alpha, output_path)

# フレームの入ったディレクトリのパス
frame_directory = "./output_frames"
process_frames_in_directory(frame_directory, alpha=0.5)