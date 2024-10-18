from pathlib import Path

import cv2
import numpy as np
import matplotlib.pyplot as plt


dark_frame_path = Path("/home/jhand/projects/rosbags/plank/star_tracking_darkframe/star_tracking_darkframe_0.mcap_pngs_imu/imx_cam2/imx678")

frames = np.asarray([cv2.imread(str(p)) for p in dark_frame_path.glob("*.png")])
mean_frame = np.uint8(np.mean(frames, axis=0))
plt.imshow(mean_frame)
plt.show()

cv2.imwrite("darkframe.png", mean_frame)
