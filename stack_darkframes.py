from pathlib import Path
from argparse import ArgumentParser
import cv2
import numpy as np
import matplotlib.pyplot as plt

parser = ArgumentParser()
parser.add_argument(
    "-i", "--input",
    help="Path to dark frame images."
)
args = parser.parse_args()

dark_frame_path = Path(args.input)
if not dark_frame_path.is_dir():
    raise ValueError("Dark frame image path does not exist.")

frames = np.asarray([cv2.imread(str(p)) for p in dark_frame_path.glob("*.png")])
mean_frame = np.uint8(np.mean(frames, axis=0))
plt.imshow(mean_frame)
plt.show()

cv2.imwrite("darkframe.png", mean_frame)
