import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

dir=input()    # l:left(counterclockwise) , r:right(clockwise)
count=float(input())
while True:
    if count<=0:
        break
    if dir=="l":
        for i in range(4):
          for j in range(4):
            if i == j:
              GPIO.output(31+2*j, GPIO.HIGH)
            else:
              GPIO.output(31+2*j, GPIO.LOW)
          time.sleep(0.01)
    elif dir=="r":
      for i in range(4):
          for j in range(4):
            if (i+j)%4 == 0:
              GPIO.output(31+2*j, GPIO.HIGH)
            else:
              GPIO.output(31+2*j, GPIO.LOW)
          time.sleep(0.01)
    count-=0.04
