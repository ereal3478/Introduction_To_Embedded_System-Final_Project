import time
import RPi.GPIO as GPIO

def ServoMotor():
  p = GPIO.PWM(32, 50)
  p.start(0)
  count = 8.75
  dir = 0.25
  done = 0
  while True:
      if count == 12:
          dir = -0.25
          time.sleep(1)
      elif count == 8.75:
          dir = 0.25
          done += 1
          time.sleep(2)
      if done == 2:
        break
      p.ChangeDutyCycle(count)
      count += dir
      time.sleep(0.00001)

