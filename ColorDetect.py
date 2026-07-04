import cv2
import numpy as np

def checkColor(image):
    #w = image.shape[0]//4
    #h = image.shape[1]//4
    #img = image[w: 3*w, h:3*h]#check
    #cv2.imshow("cut_image", image)
    #cv2.waitKey(0)
    HSVimg=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    colors =np.array(['red','green','blue'])#check
    masks=np.array([[165,70,46,179,255,255],[35,43,46,77,255,255],[100,43,46,124,255,255]])
    #check
    color_max = []
    s = 0
    for i, mask in enumerate(masks):
        output = cv2.inRange(HSVimg, mask[0:3], mask[3:6])
        '''if i == 0:
          output2 = cv2.inRange(HSVimg, (165,43,46), (179, 255, 255))
          s = np.sum(output2)'''
        sum = np.sum(output) + s
        color_max.append(sum)
    if max(color_max) < 20000000:
        print('Color not identified')
        return None, 'Not identified'
    else:
        i = color_max.index(max(color_max))
        print(str(colors[i]))
        return i, str(colors[i])
