#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 键盘输入0~100之间的值，得到不同的风扇速度。用于测试风扇。

import RPi.GPIO as GPIO
import time
import sys

FAN_PIN = 17
WAIT_TIME = 1
PWM_FREQ =25

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)

fan=GPIO.PWM(FAN_PIN,PWM_FREQ)
fan.start(0);

try:
    while 1:
        fanSpeed=float(input("Fan Speed: "))  # 获取键盘值 (#1)
        fan.ChangeDutyCycle(fanSpeed)         # 控制不同的风扇速度(#2)
        time.sleep(2)

except(KeyboardInterrupt):
    print("Fan ctrl interrupted by keyboard")
    GPIO.cleanup()
    sys.exit()
    
