#!/usr/bin/env python
from time import sleep
import serial
import os
import RPi.GPIO as GPIO
import curses

##set the GPIO pins for motor drivers 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.output(35, GPIO.LOW)
GPIO.output(37, GPIO.LOW)
GPIO.output(36, GPIO.LOW)
GPIO.output(38, GPIO.LOW)

##set the serial port settings
ser = serial.Serial(
  port='/dev/ttyAMA0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)


stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
f = open("/tmp/pythonlog","w")
stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
try:
  while key != ord('z'):
      key = stdscr.getch()
      stdscr.addch(20,25,key)
      stdscr.refresh()
      if key == curses.KEY_UP: 
          stdscr.addstr(2, 20, "Up")
          print ("hello up") 
          f.write("hello up\n")
          f.flush()
          GPIO.output(35, GPIO.LOW)
          GPIO.output(37, GPIO.HIGH)
          GPIO.output(36, GPIO.HIGH)
          GPIO.output(38, GPIO.LOW)
      elif key == curses.KEY_DOWN: 
          stdscr.addstr(3, 20, "Down")
          print ("hello down") 
          f.write("hello down\n")
          f.flush()
          GPIO.output(35, GPIO.HIGH)
          GPIO.output(37, GPIO.LOW)
          GPIO.output(36, GPIO.LOW)
          GPIO.output(38, GPIO.HIGH)
      elif key == curses.KEY_LEFT:
          stdscr.addstr(3, 20, "left")
          print ("hello left")
          f.write("hello left\n")
          f.flush()
          GPIO.output(35, GPIO.HIGH)
          GPIO.output(37, GPIO.HIGH)
          GPIO.output(36, GPIO.HIGH)
          GPIO.output(38, GPIO.LOW)
      elif key == curses.KEY_RIGHT: 
          stdscr.addstr(3, 20, "right")
          print ("hello right")
          f.write("hello left\n")
          f.flush()
          GPIO.output(35, GPIO.LOW)
          GPIO.output(37, GPIO.HIGH)
          GPIO.output(36, GPIO.HIGH)
          GPIO.output(38, GPIO.HIGH)

      elif key == ord('f'):
          stdscr.addstr(3, 20, "f")
          print ("f")
          f.write("hello f\n")
          f.flush()
          GPIO.output(35, GPIO.HIGH)
          GPIO.output(37, GPIO.HIGH)
          GPIO.output(36, GPIO.HIGH)
          GPIO.output(38, GPIO.HIGH)
      elif key == curses.KEY_HOME:
          stdscr.addstr(3, 20, "home")
          print ("hello home")
          f.write("hello home\n")
          f.flush()
      elif key == ord('q'):
          stdscr.addstr(3, 20, "f")
          print ("f")
          f.write("hello f\n")
          f.flush()
          ser.write('q')
      elif key == ord('w'):
          stdscr.addstr(3, 20, "f")
          print ("f")
          f.write("hello f\n")
          f.flush()
          ser.write('w')
      elif key == ord('e'):
          stdscr.addstr(3, 20, "f")
          print ("f")
          f.write("hello f\n")
          f.flush()
          ser.write('e')
  GPIO.output(35, GPIO.HIGH)
  GPIO.output(37, GPIO.HIGH)
  GPIO.output(36, GPIO.HIGH)
  GPIO.output(38, GPIO.HIGH)
finally:

  curses.endwin()

