#!/bin/bash

#locale
# 修改如下路径到应用所在的位置
app_path=/home/pi/Workspace/rpi_fan_ctrl
app=fan_ctrl

cd $app_path
# 运行应用
sudo python3 fan_ctrl.py

# with source start up
#sudo python3 fan_ctrl.py
#cd ~ 
