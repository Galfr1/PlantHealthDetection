# Plant Health Detection

This software is used while detecting the plant's health while its in the frame.

There are 2 python files in this project:
 - one that let you capture a frame and then analyze it ('frames.py').
 - one thats doing live video detection after pressing the 'begin' button ('loop.py').
 
 This project can run on all platforms:
  - MacOS
  - Linux
  - Windows
  
  For this project to run you will need:
  - OpenCV (python)
  - TensorFlow (python)
  - python 3
  - PIL
  - numpy
  
#OpenCV Installation On Raspberry Pi That Runs Raspberry Pi OS

On raspberry pi os there are a few extra steps for installing opencv (they are requierd).
Install OpenCV with the following commands:

sudo apt-get update && sudo apt-get upgrade

sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev

pip install opencv-contrib-python

pip install pillow

pip install imutils
