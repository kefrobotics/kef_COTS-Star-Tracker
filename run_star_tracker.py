import os
import csv
import json
import time
import psutil
import subprocess
from pathlib import Path
import yaml

import numpy as np
from datetime import datetime
from star_tracker import main
from star_tracker.cam_matrix import read_cam_json
from star_tracker.array_transformations import *


config_path = Path("config") / "darkframe.yaml"
with open(config_path, "r") as fp:
    config_dict = yaml.safe_load(fp)

starMatchPixelTol = config_dict["starMatchPixelTol"]
min_star_area = config_dict["min_star_area"]
max_star_area = config_dict["max_star_area"]
nmatch = config_dict["nmatch"]
low_thresh_pxl_intensity = config_dict["low_thresh_pxl_intensity"]
hi_thresh_pxl_intensity = config_dict["hi_thresh_pxl_intensity"]

VERBOSE = config_dict["VERBOSE"]
data_path = Path(config_dict["data_path"])
catalog_path = Path(config_dict["catalog_path"])
cam_config_file = Path(config_dict["cam_config_file"])
darkframe_file = Path(config_dict["darkframe_file"])

# Create new output directory in input data directory
init_time = str(datetime.now())
init_time = init_time.split(".")
init_time = init_time[0]
init_time = init_time.replace(" ", "_")
init_time = init_time.replace(":", "-")
new_output_dir = data_path / init_time
new_output_dir.mkdir(exist_ok=False)

# Load catalog matrices.
k = np.load(catalog_path / "k.npy")
m = np.load(catalog_path / "m.npy")
q = np.load(catalog_path / "q.npy")
x_cat = np.load(catalog_path / "u.npy")
indexed_star_pairs = np.load(catalog_path / "indexed_star_pairs.npy")

# Load
camera_matrix, _, _ = read_cam_json(str(cam_config_file))
dx = camera_matrix[0, 0]
isa_thresh = starMatchPixelTol / dx

#run star tracker
solve_start_time = time.time()
for img_path in data_path.glob("*.jpg"):
    q_est, idmatch, nmatches, x_obs, rtrnd_img = main.star_tracker(
        str(img_path), str(cam_config_file), darkframe_file=darkframe_file,
        m=m, q=q, x_cat=x_cat, k=k, indexed_star_pairs=indexed_star_pairs, graphics=False,
        min_star_area=min_star_area, max_star_area=max_star_area, isa_thresh=isa_thresh, nmatch=nmatch
    )

solve_time += [time.time() - solve_start_time]
