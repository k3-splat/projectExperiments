import cv2
import numpy as np

prev_frame = cv2.imread("./output_frames/frame_0000.png", cv2.IMREAD_GRAYSCALE)
next_frame = cv2.imread("./output_frames/frame_0005.png", cv2.IMREAD_GRAYSCALE)

flow = cv2.calcOpticalFlowFarneback(prev_frame, next_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)
alpha = 0.5

h, w = prev_frame.shape
flow_x, flow_y = flow[..., 0] * alpha, flow[..., 1] * alpha
map_x, map_y = np.meshgrid(np.arange(w), np.arange(h))
map_x = (map_x + flow_x).astype(np.float32)
map_y = (map_y + flow_y).astype(np.float32)

interpolated_frame = cv2.remap(prev_frame, map_x, map_y, interpolation=cv2.INTER_LINEAR)
blended_frame = cv2.addWeighted(interpolated_frame, 1 - alpha, next_frame, alpha, 0)

cv2.imwrite("interpolated_frame.png", blended_frame)