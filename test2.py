from pymouse import *
import time
import win32api
import pyautogui

import cv2
import numpy as np
from PIL import ImageGrab

def autoguiHoldOn(x,y,t):
    pyautogui.moveTo(x,y)
    goOneStepWithTime(x,y,t)

def getScreenArray():
    img = ImageGrab.grab(bbox=(0, 0, 2048, 2048))
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
    # cv2.imshow("222",img)
    cv2.waitKey(0)
    return img

def press(x, y, button=1):
    buttonAction = 2 ** ((2 * button) - 1)
    win32api.mouse_event(buttonAction, x, y)


def release(x, y, button=1):
    buttonAction = 2 ** ((2 * button))
    win32api.mouse_event(buttonAction, x, y)


def click(x, y, button=1):
    press(x, y, button)
    release(x, y, button)


def goOneStepWithTime(x,y,t):
    press(x,y)
    time.sleep(t)
    release(x,y)
    print(f"running one step done. Position: ({x},{y}); for {t} s.")


def getTimefromDistance(distance):
    return 3.5*distance

# def handCraftMeasure():
    ## get src position
    # if

def getWindowPosition(all_array, window_array):
    print("shape of window array：", window_array.shape)
    h,w=window_array.shape

    meth="cv2.TM_CCOEFF"
    method=eval(meth)
    results=cv2.matchTemplate(all_array,window_array,method)
    min_val,max_val,min_loc,top_left=cv2.minMaxLoc(results)
    bottom_right=(top_left[0] + w, top_left[1] + h)

    return top_left, bottom_right


def mymain():
    # get all screen
    screen_array=getScreenArray()
    screen_array = cv2.cvtColor(screen_array, cv2.COLOR_BGR2GRAY)

    ## get game position
    screen=cv2.imread("./screen.png")
    screen= cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen_p_tl,screen_p_br=getWindowPosition(screen_array,screen)

    print(f"Window top-left posotion: {screen_p_tl}")
    print(f"Window bottom-right posotion: {screen_p_br}")
    screen_p_tl=(735,142)
    screen_p_br=(1185,941)
    centerx=int((screen_p_tl[0]+screen_p_br[0])/2)
    centery=int((screen_p_tl[1]+screen_p_br[1])/2)
    # centerx+=200
    # centery+=100

    person=cv2.imread("./person.png")
    person = cv2.cvtColor(person, cv2.COLOR_BGR2GRAY)
    per_p_tl,per_p_br=getWindowPosition(screen_array,person)
    
    print(f"person top-left posotion: {per_p_tl}")
    print(f"person bottom-right posotion: {per_p_br}")

    srcx=per_p_tl[0]+16
    srcy=per_p_tl[1]+79

    # srcx=per_p_tl[0]+src
    # srcy=per_p_tl[1]+79
    # # srcx=875
    # srcy=602
    # srcx-=4
    # srcy-=4

    print(f"person position: ({srcx},{srcy})")

    point=np.array([srcx-centerx,srcy-centery])

    ## calculate distance
    distance=np.linalg.norm(point)
    t=getTimefromDistance(distance)/1000
    print(f"planning time: {t}")

    # goOneStepWithTime(centerx,centery,t)
    autoguiHoldOn(srcx,srcy,t)


def handwork(centerx,centery):
    # get all screen
    screen_array=getScreenArray()
    screen_array = cv2.cvtColor(screen_array, cv2.COLOR_BGR2GRAY)

    ## get game position
    screen=cv2.imread("./screen.png")
    screen= cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen_p_tl,screen_p_br=getWindowPosition(screen_array,screen)

    print(f"Window top-left posotion: {screen_p_tl}")
    print(f"Window bottom-right posotion: {screen_p_br}")
    screen_p_tl=(735,142)
    screen_p_br=(1185,941)
    # centerx=int((screen_p_tl[0]+screen_p_br[0])/2)
    # centery=int((screen_p_tl[1]+screen_p_br[1])/2)
    # centerx+=200
    # centery+=100

    person=cv2.imread("./person.png")
    person = cv2.cvtColor(person, cv2.COLOR_BGR2GRAY)
    per_p_tl,per_p_br=getWindowPosition(screen_array,person)
    
    print(f"person top-left posotion: {per_p_tl}")
    print(f"person bottom-right posotion: {per_p_br}")

    srcx=per_p_tl[0]+16
    srcy=per_p_tl[1]+79

    print(f"person position: ({srcx},{srcy})")

    point=np.array([srcx-centerx,srcy-centery])

    ## calculate distance
    distance=np.linalg.norm(point)
    t=getTimefromDistance(distance)/1000
    print(f"planning time: {t}")

    # goOneStepWithTime(centerx,centery,t)
    autoguiHoldOn(srcx,srcy,t)



def getPosition():
    m=PyMouse()
    print(m.position())
    return m.position()

def main():
    i=0
    while True:
        if i>5000000:
            break
        mymain()
        i+=1

def main1():
    i=0
    while True:
        print("please set your persition")
        y=input("enter g to set done. and q to exit.")
        if y=="":
            persition=getPosition()
            handwork(persition[0],persition[1])
        else:
            return 0
        
        if i>5000000:
            break
        # mymain()
        i+=1

# main()
main1()
# mymain()
# getPosition()
