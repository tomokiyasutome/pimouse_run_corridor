#!/bin/bash -xve

#syync and make
rsync -av ./ ~/catkin_ws/src/pimouse_ros/
cd ~/catkin_ws/src/
git clone --depth=1  git@github.com:tomokiyasutome/pimouse_ros.git

cd ~/catkin_ws
catkin_make
