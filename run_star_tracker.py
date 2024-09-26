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
from star_tracker.cam_matrix import *
from star_tracker.array_transformations import *

config_path = Path("config") / "darkframe.yaml"
with open(config_path, "r") as fp:
    config_dict = yaml.safe_load(fp)

starMathPixelTol = config_dict["starMatchPixelTol"]
min_star_area = config_dict["min_star_area"]
max_star_area = config_dict["max_star_area"]
nmatch = config_dict["nmatch"]
low_thresh_pxl_intensity = config_dict["low_thresh_pxl_intensity"]
hi_thresh_pxl_intensity = config_dict["hi_thresh_pxl_intensity"]

VERBOSE = config_dict["VERBOSE"]
data_path = config_dict["data_path"]
catalog_path = config_dict["catalog_path"]
cam_config_file = config_dict["cam_config_file"]

init_time = str(datetime.now())
init_time = init_time.split('.')
init_time = init_time[0]
init_time = init_time.replace(' ','_')
init_time = init_time.replace(':','-')
new_output_dir = os.path.join(data_dir,  init_time )
os.mkdir(the_dir)