import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(32,GPIO.OUT)

p = GPIO.PWM(32, 50)
p.start(0)
count = 8.75
dir = 0.25
while True:
    if count == 12:
        dir = -0.25
        time.sleep(1.5)
    if count == 8.75:
        dir = 0.25
        time.sleep(3.5)
    p.ChangeDutyCycle(count)
    count += dir
    time.sleep(0.00001)
