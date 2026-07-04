import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

while True:
	GPIO.output(31,GPIO.HIGH)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(37,GPIO.LOW)
	time.sleep(0.01)
	GPIO.output(31,GPIO.LOW)
	GPIO.output(33,GPIO.HIGH)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(37,GPIO.LOW)
	time.sleep(0.01)
	GPIO.output(31,GPIO.LOW)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.HIGH)
	GPIO.output(37,GPIO.LOW)
	time.sleep(0.01)
	GPIO.output(31,GPIO.LOW)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(37,GPIO.HIGH)
	time.sleep(0.01)








 
