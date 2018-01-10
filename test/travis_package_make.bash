#!/bin/bash -xve

#syync and make
rsync -av ./ ~/catkin_ws/src/pimouse_run_corridor/
cd ~/catkin_ws/src/
git clone  https://github.com/tomokiyasutome/pimouse_ros.git

cd ~/catkin_ws
catkin_make
