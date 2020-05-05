#!/bin/bash

# 服务名称.
app=fan_ctrl

chmod 755 ./run.sh
chmod 755 ./$app
chmod 644 ./$app.service 
sudo cp ./$app.service /lib/systemd/system/
sudo systemctl daemon-reload
systemctl status $app.service
