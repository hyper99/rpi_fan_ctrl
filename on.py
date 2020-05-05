#!/usr/bin/python
# -*- coding: utf-8 -*-
# 用于测试风扇。

import RPi.GPIO as GPIO
import time
import sys
import psutil

FAN_PIN = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.HIGH)
try:
    while 1:
        cpuTemp = psutil.sensors_temperatures()['cpu-thermal'][0].current # 用psutil取温度
        print(cpuTemp)
        time.sleep(2)
except(KeyboardInterrupt):
    GPIO.cleanup()
    sys.exit()
    
