
import cv2
import numpy as np
#print [i for i in dir(cv2) if 'EVENT' in i]             #gives all events fron dirctory which cintains keywkord event

img=np.zeros((320,320,3),np.uint8)
print img.shape

def onClickfunc(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        if x in range(10,111) and y in range(10,111):
            print x,y,1
            func(60,60,1)
        elif x in range(111,211) and y in range(10,111):
            print x,y,2
            func(160,60,2)
        elif x in range(211,311) and y in range(10,111):
            print x,y,3
            #cv2.circle(img,(a,b),10,(0,255,0),8)
            func(260,60,3)
        elif x in range(10,111) and y in range(111,211):
            print x,y,4
            func(60,160,4)
        elif x in range(111,211) and y in range(111,211):
            print x,y,5
            func(160,160,5)
        elif x in range(211,311) and y in range(111,211):
            print x,y,6
            func(260,160,6)
        elif x in range(10,111) and y in range(211,311):
            print x,y,7
            func(60,260,7)
        elif x in range(111,211) and y in range(211,311):
            print x,y,8
            func(160,260,8)
        elif x in range(211,311) and y in range(211,311):
            print x,y,9
            func(260,260,9)
'''
def mod(k):
    if k==0:
       
    
 '''       
def clicked(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONUP:
        print 56
        print(x,y)                                          #gives coord where mouse click occurs

def comp(li):
    l=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    for i in range(0,9):
        n=0
        for val in l[i]:
            if val not in li:
                break
            else:
                n+=1
        if n==3:
            return 1
    return 0
        


cv2.line(img,(10,110),(310,110),(255,0,0),3)
cv2.line(img,(10,210),(310,210),(255,0,0),3)
cv2.line(img,(110,10),(110,310),(255,0,0),3)
cv2.line(img,(210,10),(210,310),(255,0,0),3)

l1=[]
l2=[]


g=raw_input("enter 1st player name ")
h=raw_input("enter 2nd player name ")
global a,b,c
def func(p,q,r):
    m=0
    fg=0
    if fg==0 and m<9:
        m+=1
        if m%2==0:
            print p,q,r
            l1.append(r)
            l1.sort()
            cv2.circle(img,(p,q),10,(0,255,0),8)
            fg=comp(l1)
        else:
            print p,q,r
            l2.append(r)
            l2.sort()
            cv2.line(img,(p-20,q-20),(p+20,q+20),(0,0,255),2)
            cv2.line(img,(p-20,q+20),(p+20,q-20),(0,0,255),2)
            fg=comp(l2)
        if fg==1 and m%2==0:
            print h,' is the winner'
            cv2.destroyAllWindows()
        elif fg==1 and m%2!=0:
            print g,' is the winner'
            cv2.destroyAllWindows()
		
a = b = c = 0
		
cv2.namedWindow('frame')
cv2.imshow('frame',img)
cv2.setMouseCallback('frame',onClickfunc)
cv2.waitKey(0)
cv2.destroyAllWindows()


                
