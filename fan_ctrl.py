#!/usr/bin/python
# -*- coding: utf-8 -*-
# PWM温控风扇程序
# by hyper99, 790516@qq.com

import RPi.GPIO as GPIO
import time
import sys
import psutil

# Configuration
FAN_PIN = 17            # GPIO17,可以自己修改为其它GPIO引脚。(#1)
WAIT_TIME = 3           # [s] Time to wait between each refresh 1s
PWM_FREQ = 25           # [Hz] Change this value if fan has strange behavior

# Configurable temperature and fan speed steps
T_MIN = 45 # start fan at FAN_MIN% PWM
T_MAX = 50 # fan 100% PWM
FAN_MIN = 70  # 70% 
FAN_MAX = 90  # 90%
N  = 10
tempSteps = [T_MIN + i*(T_MAX -T_MIN)/N for i in range(N + 1)] #  温控上下界， 45~50
speedSteps = [FAN_MIN + i*(FAN_MAX - FAN_MIN)/N for i in range(N + 1)] # PWM占空比70%~100% 

#fanSpeed = FAN_MIN + (cpuTemp - T_MIN)*(100 - FAN_MIN)/(T_MAX - T_MIN)  # [45,50]~[70,100]
a = FAN_MIN - T_MIN*(FAN_MAX - FAN_MIN)/(T_MAX - T_MIN)
b = (FAN_MAX - FAN_MIN)/(T_MAX - T_MIN)
#fanSpeed = a + b*cpuTemp

# var
hyst = 1
cpuTemp  =0 
cpuTempOld=0
fanSpeed = 0
fanSpeedOld=0

# Setup GPIO pin
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)
fan=GPIO.PWM(FAN_PIN,PWM_FREQ)  # pwm方式工作
fan.start(0)

# test fan at beginning 
fan.ChangeDutyCycle(100)
time.sleep(5)
fan.ChangeDutyCycle(0)

# show current temperature and range
cpuTemp = psutil.sensors_temperatures()['cpu-thermal'][0].current # 用psutil取温度
print("Current Temperature:{}".format(cpuTemp))
print("minTemp = {}; maxTemp = {}".format(T_MIN, T_MAX))

 
while (1):
    # Read CPU temperature
    #cpuTempFile=open("/sys/class/thermal/thermal_zone0/temp","r")
    #cpuTemp=float(cpuTempFile.read())/1000
    #cpuTempFile.close()
    cpuTemp = psutil.sensors_temperatures()['cpu-thermal'][0].current # 用psutil取温度
    #print(cpuTemp) 
    # Calculate desired fan speed
    if(abs(cpuTemp-cpuTempOld) > hyst):
        cpuTempOld = cpuTemp 
        # Below first value, fan will stop.
        if(cpuTemp < T_MIN):
           fanSpeed = 0 # stop fan

       # Above last value, fan will run at max speed
        elif(cpuTemp >= T_MAX):
           fanSpeed =  100

        # If temperature is between 2 steps, fan speed is calculated by linear interpolation
        else:       
            #fanSpeed = FAN_MIN + (cpuTemp - T_MIN)*(FAN_MAX - FAN_MIN)/(T_MAX - T_MIN)  # [45,50]~[70,90]
            fanSpeed = a + b*cpuTemp
        if(fanSpeed != fanSpeedOld):
            print("T: {}".format(cpuTemp))
            print("Fan PWM: {}".format(fanSpeed))
            fan.ChangeDutyCycle(fanSpeed)
            fanSpeedOld = fanSpeed                

    # Wait until next refresh
    time.sleep(WAIT_TIME)

 


