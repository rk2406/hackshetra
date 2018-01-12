import cv2
import numpy as np #to perform some complex mathematical operations

'''img=cv2.imread('image.jpg')#reading image

#shows the image on a screen/container...we create a container like a window on our laptop
#cv2.named('frame1',cv2.WINDOW_NORMAL)#creating a new window ...creates a window of normal size
cv2.imshow('frame1',img)
cv2.waitKey(2000)#waits for user to press any key... here it is zero that is infinite time... if we write an integer thrn it gets destroyed automatically after that much time
cv2.destroyAllWindows()#all frame windows gets destroyed... to close the windows
cv2.imwrite('python/newimg.jpg',img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
print img.shape
print img.size'''

img=np.zeros((300,300,3),np.uint8)#each of the three values have the color space stored as BGR .... this is a collection of lists
#here 300X300 is the resolution and 3 is the number of channels... whenever we try to define an image... we can count values from 0 to 255 uint8 means it has a value of 8 bit each
#cv2.line(image,start,end,color(BGR),thickness)
#cv2.line(img,(100,100),(200,200),(255,0,0),5)
#cv2.line(image,start of diagnol,end of diagnol,color(BGR),thickness)
#cv2.rectangle(img,(100,100),(150,250),(0,255,255),-3)
#center of circle and radius
#cv2.circle(img,(100,100),25,(255,255,0),-1)
font=cv2.FONT_HERSHEY_SIMPLEX
#(img,string to be displayed,starting position, font,font scale(0-1),color,thickness)
cv2.putText(img,'EmR CLUB',(100,100),font,0.8,(255,255,0),4)
cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroysAllWindows()
