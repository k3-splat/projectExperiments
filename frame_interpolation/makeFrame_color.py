import cv2
import numpy as np

# 前フレームと後フレームの読み込み（カラー画像）
prev_frame = cv2.imread("./output_frames/frame_0000.png")
next_frame = cv2.imread("./output_frames/frame_0010.png")

# 各チャンネル（B, G, R）に分けて処理
channels = cv2.split(prev_frame)
next_channels = cv2.split(next_frame)

alpha = 0.5
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
cv2.imwrite("color_interpolated_frame.png", color_interpolated_frame)