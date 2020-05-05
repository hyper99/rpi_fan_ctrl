# rpi_fan_ctrl
Raspberry pi pwm fan control with temperature detection.


## 1. install service
> sudo ./install_service.sh
 
## 2. start/stop service

> systemctl start   fan_ctrl.service # start service
> systemctl stop    fan_ctrl.service # stop service
> systemctl enable  fan_ctrl.service # power on enable
> systemctl disable fan_ctrl.service # power on disable
> systemctl status  fan_ctrl.service # display service status
> systemctl show    fan_ctrl.service # display service parameters

