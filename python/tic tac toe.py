import cv2
import numpy as np

'''print[i for i in dir(cv2)if 'EVENT' in i]'''#i checks thw stringword directory and checks if the event keyword is present or not we are accessing those events
#that have the keyword event in them
def onClickfunc(event,x,y,flags,param):#whenever we lift the button the coordinates get printed on console
    if event==cv2.EVENT_LBUTTONUP:
        print(x,y)

img=cv2.imread('image.jpg')
cv2.namedWindow('frame')
cv2.imshow('frame',img)
cv2.setMouseCallback('frame',onClickfunc)#setting an event list  whenever some even thappens it causes the event listener to captures that event and forward to another
#function which will be processed by thee user... mousecallback listener reacts only to mouse clicks....all the events will be forwarded to onclickfunc
cv2.waitKey(0)
cv2.destroyAllWindows()
