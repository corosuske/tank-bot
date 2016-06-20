#!/usr/bin/env python
from time import sleep
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)           
GPIO.setup(5, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.output(3, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
GPIO.output(8, GPIO.LOW)
GPIO.output(10, GPIO.LOW)

while True:
        GPIO.output(3, GPIO.HIGH)
	GPIO.output(5, GPIO.LOW)
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(10, GPIO.LOW)
	sleep(3);
        GPIO.output(3, GPIO.LOW)
	GPIO.output(5, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)
        GPIO.output(10, GPIO.HIGH)
	sleep(3)

