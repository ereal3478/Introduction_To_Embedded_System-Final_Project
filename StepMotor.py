import time
import RPi.GPIO as GPIO


#dir=input()    # l:left(counterclockwise) , r:right(clockwise)
#count=int(input())
def StepMotor(prev, cur):
  t = 2
  '''
  1 0
  1 2
  0 1
  0 2
  '''
  if cur > prev:
    dir = "r"
  else:
    dir = "l"
  count = abs(cur-prev)*t
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
