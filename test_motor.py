import time
import threading
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(32,GPIO.OUT)#servo
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

def job(num):
    if num==0:
        Rotate()
    elif num==1:
        Spin()

def Rotate():
    p = GPIO.PWM(32, 50)
    p.start(0)
    count = 2 
    dir = 1
    while True:        
        if count == 8: 
            dir = -1
            time.sleep(2) 
        if count == 2: 
            dir = 1 
            time.sleep(4)
        p.ChangeDutyCycle(count)
        count += dir
        time.sleep(0.01)

def Spin():
    dir=0
    count=6
    while True:
        if count<=0:
            count=6
            dir = 1-dir
            time.sleep(5)
        if dir==0:
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
        elif dir==1:
            GPIO.output(31,GPIO.HIGH)
            GPIO.output(33,GPIO.LOW)
            GPIO.output(35,GPIO.LOW)
            GPIO.output(37,GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(31,GPIO.LOW)
            GPIO.output(33,GPIO.LOW)
            GPIO.output(35,GPIO.LOW)
            GPIO.output(37,GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(31,GPIO.LOW)
            GPIO.output(33,GPIO.LOW)
            GPIO.output(35,GPIO.HIGH)
            GPIO.output(37,GPIO.LOW)
            time.sleep(0.01)
            GPIO.output(31,GPIO.LOW)
            GPIO.output(33,GPIO.HIGH)
            GPIO.output(35,GPIO.LOW)
            GPIO.output(37,GPIO.LOW)
            time.sleep(0.01)
        count-=0.05

threads=[]
for i in range(2):
    threads.append(threading.Thread(target=job,args=(i,)))
    threads[i].start()
for i in range(2):
    threads[i].join()


