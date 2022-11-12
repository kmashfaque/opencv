# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

#img1=cv2.imread("C:\\Users\\HP\\Desktop\\OpenCV\\HappyFish.jpg",1)
#img1 = cv2.resize(img1,(500,700))#width ,height
#cv2.imshow("colored image",img1)

#img3 = cv2.imread('C:\\Users\\HP\\Desktop\\OpenCV\\HappyFish.jpg',-1)
#img3 = cv2.resize(img3,(1280,700))#width ,height
#cv2.imshow("Original Image",img3)
#print("Image in original value==\n",img3)

#cv2.waitKey(0)
#cv2.destroyAllWindows()



img2=cv2.imread("C:\\Users\\HP\\Desktop\\OpenCV\\HappyFish.jpg",1)
img2=cv2.resize(img2,(560,700))
img2=cv2.flip(img2,0)
cv2.imshow("converted image==",img2)
k=cv2.waitKey(0) & 0xFF

if k==ord("q"):
    cv2.destroyAllWindows()

elif k==ord("s"):
    cv2.imwrite("C:\\Users\\HP\\Desktop\\OpenCV\\HappyFish2.jpg",img2)
    cv2.destroyAllWindows()