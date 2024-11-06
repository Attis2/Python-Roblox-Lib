# Useless

import os
import shutil

def remove_egg_info_dirs():
    current_dir = os.getcwd()
    for item in os.listdir(current_dir):
        if item.endswith('.egg-info'):
            shutil.rmtree(item)
            print(f"Removed directory: {item}")

remove_egg_info_dirs()