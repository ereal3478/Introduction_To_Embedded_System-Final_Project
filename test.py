import time
import RPi.GPIO as GPIO
import Motor

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(32,GPIO.OUT)

Motor.Rotate("red")















































