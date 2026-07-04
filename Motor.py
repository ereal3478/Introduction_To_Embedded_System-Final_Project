
import time
import RPi.GPIO as GPIO

def Rotate(color):
    if color == 'red':
        p = GPIO.PWM(32, 50)
        p.start(0)
        count = 1 
        dir = 1
        while True:        
            if count == 10: 
                dir = -1
                time.sleep(5) 
            if count == 2: 
                dir = 1 
                time.sleep(1)
            p.ChangeDutyCycle(count)
            count += dir
            time.sleep(0.05)          

    elif color == 'green':
        pass
    elif color == 'blue':
        pass
    elif color == 'cyan':
        pass
    else:
        pass
