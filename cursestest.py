#!/usr/bin/env python
from time import sleep
import os
import RPi.GPIO as GPIO
import curses
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.output(3, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
GPIO.output(8, GPIO.LOW)
GPIO.output(10, GPIO.LOW)



stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
f = open("/tmp/pythonlog","w")
stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
try:
  while key != ord('q'):
      key = stdscr.getch()
      stdscr.addch(20,25,key)
      stdscr.refresh()
      if key == curses.KEY_UP: 
          stdscr.addstr(2, 20, "Up")
          print ("hello up") 
          f.write("hello up\n")
          f.flush()
          GPIO.output(3, GPIO.LOW)
          GPIO.output(5, GPIO.HIGH)
          GPIO.output(8, GPIO.HIGH)
          GPIO.output(10, GPIO.LOW)
      elif key == curses.KEY_DOWN: 
          stdscr.addstr(3, 20, "Down")
          print ("hello down") 
          f.write("hello down\n")
          f.flush()
          GPIO.output(3, GPIO.HIGH)
          GPIO.output(5, GPIO.LOW)
          GPIO.output(8, GPIO.LOW)
          GPIO.output(10, GPIO.HIGH)
      elif key == curses.KEY_LEFT:
          stdscr.addstr(3, 20, "left")
          print ("hello left")
          f.write("hello left\n")
          f.flush()
          GPIO.output(3, GPIO.HIGH)
          GPIO.output(5, GPIO.HIGH)
          GPIO.output(8, GPIO.HIGH)
          GPIO.output(10, GPIO.LOW)
      elif key == curses.KEY_RIGHT: 
          stdscr.addstr(3, 20, "right")
          print ("hello right")
          f.write("hello left\n")
          f.flush()
          GPIO.output(3, GPIO.LOW)
          GPIO.output(5, GPIO.HIGH)
          GPIO.output(8, GPIO.HIGH)
          GPIO.output(10, GPIO.HIGH)

      elif key == ord('f'):
          stdscr.addstr(3, 20, "f")
          print ("f")
          f.write("hello f\n")
          f.flush()
          GPIO.output(3, GPIO.HIGH)
          GPIO.output(5, GPIO.HIGH)
          GPIO.output(8, GPIO.HIGH)
          GPIO.output(10, GPIO.HIGH)
  GPIO.output(3, GPIO.HIGH)
  GPIO.output(5, GPIO.HIGH)
  GPIO.output(8, GPIO.HIGH)
  GPIO.output(10, GPIO.HIGH)
finally:

  curses.endwin()



