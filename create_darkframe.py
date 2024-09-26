#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import cv2
from pathlib import Path
import yaml
import time
import star_tracker.ground as ground


config_path = Path("config") / "darkframe.yaml"
with open(config_path, "r") as fp:
    config_dict = yaml.safe_load(fp)

path_to_images = config_dict["img_directory"]
num_images = config_dict["n_imgs"]

# CREATE DARK FRAME
print("\ncreating dark frame...")
start_time = time.time()

# img_list = ground.find_files_pattern(im_pattern, im_path, exclude='dark')
img_list = [
    os.path.join(path_to_images, f) for f in os.listdir(path_to_images)
    if os.path.isfile(os.path.join(path_to_images, f))
]

if len(img_list) < 1:
    print("No images found, unable to create darkframe")

else:
    darkframe = ground.create_darkframe(img_list, num_images)

    # Save dark frame
    darkframe_path = os.path.join(path_to_images, 'autogen_darkframe.jpg')
    cv2.imwrite(darkframe_path, darkframe)
    print(darkframe_path)
    print("\n...dark frame creation complete in {0} seconds\n".format(time.time() - start_time))
