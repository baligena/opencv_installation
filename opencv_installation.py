import os

# works on Ubuntu 12.04.4 LTS
# follow the instructions http://www.samontab.com/web/2012/06/installing-opencv-2-4-1-ubuntu-12-04-lts/

home_path = os.path.expanduser("~")

os.system("sudo apt-get update")
os.system("sudo apt-get upgrade")
os.system("sudo apt-get install build-essential libgtk2.0-dev libjpeg-dev libtiff4-dev libjasper-dev libopenexr-dev cmake python-dev python-numpy python-tk libtbb-dev libeigen2-dev yasm libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev libqt4-dev libqt4-opengl-dev sphinx-common texlive-latex-extra libv4l-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev")

os.chdir(home_path)
os.system("wget http://downloads.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.1/OpenCV-2.4.1.tar.bz2")
os.system("tar -xvf OpenCV-2.4.1.tar.bz2")

os.chdir("OpenCV-2.4.1")
os.system("mkdir build")

os.chdir("build")
os.system("cmake -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..")
os.system("make")
os.system("sudo make install")
os.system("sudo gedit /etc/ld.so.conf.d/opencv.conf")
os.system("sudo ldconfig")
os.system("sudo gedit /etc/bash.bashrc")

print "DONE"
