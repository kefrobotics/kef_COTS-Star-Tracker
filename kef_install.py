"""
@author Jared Hand
September 2024

Most of what we need is already install in kef_env.  This script installs a
few more requirements.  Partly taken from setup/ubuntu/install.py.
"""
import os

os.system("sudo pip3 install astropy")  # required for catalog creation
os.system("sudo pip3 install statistics")
os.system("sudo pip3 install astroquery")  # required for astrometry verification

home = os.getcwd()
os.chdir("py_src/star_tracker")
os.system("sudo pip3 install .")
os.chdir(home)
