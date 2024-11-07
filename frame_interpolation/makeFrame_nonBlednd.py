import cv2
import numpy as np

# 前フレームと後フレームを読み込み
prev_frame = cv2.imread('./output_frames/frame_0005.png')
next_frame = cv2.imread('./output_frames/frame_0007.png')

# 前フレームと後フレームのサイズを確認
if prev_frame is None or next_frame is None:
    raise ValueError("前フレームまたは後フレームの読み込みに失敗しました。ファイルパスを確認してください。")

# オプティカルフロー計算のためにグレースケールに変換
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
next_gray = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)

# オプティカルフローを計算
flow = cv2.calcOpticalFlowFarneback(prev_gray, next_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

# 前フレームの各ピクセルを中間位置に移動させるためのリマップを設定
h, w = flow.shape[:2]
# ここで、x, y 座標のメッシュグリッドを作成し、flowの形に合わせてスタックします
x, y = np.meshgrid(np.arange(w), np.arange(h))
flow_map = np.stack((x, y), axis=-1).astype(np.float32) + flow

# 中間フレーム（カラー）を作成するための処理
interpolated_channels = []
for i in range(3):  # B, G, R チャンネルごとにリマップ
    interpolated_channel = cv2.remap(prev_frame[:, :, i], flow_map[:, :, 0], flow_map[:, :, 1], 
                                     interpolation=cv2.INTER_LINEAR)
    interpolated_channels.append(interpolated_channel)

# チャンネルを結合してカラー画像として中間フレームを作成
interpolated_frame = cv2.merge(interpolated_channels)

# 結果の表示
cv2.imshow('Interpolated Frame without Blending', interpolated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
