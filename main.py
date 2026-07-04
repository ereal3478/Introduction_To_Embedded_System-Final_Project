import cv2
import time
import RPi.GPIO as GPIO
import ColorDetect
import threading
import StepMotor
import ServoMotor
import LCD

video = cv2.VideoCapture(0)
FPS = 1/30
FPS_MS = int(FPS*1000)
frame = video.read()[1]

def update():
    global video, FPS, frame
    while True:
        if video.isOpened():
            frame = video.read()[1]
        time.sleep(FPS)

def show_frame():
        global frame, FPS_MS
        cv2.imshow('frame', frame)
        cv2.waitKey(FPS_MS)

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(32, GPIO.OUT)#servo motor
    GPIO.setup(31,GPIO.OUT)#step motor IN1
    GPIO.setup(33,GPIO.OUT)#step motor IN2
    GPIO.setup(35,GPIO.OUT)#step motor IN3
    GPIO.setup(37,GPIO.OUT)#step motor IN4
    
    
    
    video.set(cv2.CAP_PROP_BUFFERSIZE, 2)
    video.set(3, 1280) #width
    video.set(4, 1024) #height
    video.set(15, -13) #exposure
    
    global frame
    
    thread = threading.Thread(target = update, args=())
    thread.daemon = True
    thread.start()
    
    cur = 1
    while True:
        #colors =np.array(['red','green','blue'])#check
        #frame = video.read()[1]
        #show_frame()
        color, color_name = ColorDetect.checkColor(frame)
        LCD.LCDDisplay(color_name)
        if color == None:
          StepMotor.StepMotor(cur, 1)
          break
        StepMotor.StepMotor(cur, color)
        ServoMotor.ServoMotor()
        cur = color
  
if __name__ == "__main__":
    main()
  
  
  
  
  
  
