# # -*- coding: utf-8 -*-
# """
# Created on Sat Nov 19 20:17:13 2022

# @author: HP
# """
import cv2

# # Here with the help of videoCapture fucntion we easily ready any video.
# # cap=cv2.VideoCapture("C:\\Users\\HP\\Desktop\\OpenCV\\test2.mp4")

# # while True:
# # ret,frame=cap.read()

# # get height,weight of frame

# # print("Width==>",cv2.CAP_PROP_FRAME_WIDTH)
# # print("Height==>",cv2.CAP_PROP_FRAME_HEIGHT)

# # frame=cv2.resize(frame,(700,450))
# # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# # frame=cv2.flip(frame,-1)
# # cv2.imshow("Colorframe",frame)
# # cv2.imshow("Grayframe",gray)

# # if cv2.waitKey(1)==ord("q"):
# #   break


# # cap.release()
# # cv2.destroyAllWindows()



cap2=cv2.VideoCapture(0,cv2.CAP_DSHOW)
print("Check==>",cap2.isOpened())

#it is 4 byte code which is use to specify the video codec
#Various codec -- 
#DIVX, XVID, MJPG, X264, WMV1, WMV2


fourcc=cv2.VideoWriter_fourcc(*"XVID")

#It contain 4 parameter , name, codec,fps,resolution

output=cv2.VideoWriter("output.mp4",fourcc,20.0,(640,480),0)


while cap2.isOpened():
    ret,frame=cap2.read()
    
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #here flip is used to lip the video at recording time
        # frame=cv2.flip(frame,0)
        output.write(gray)
        
        cv2.imshow("Grayframe",gray)
        cv2.imshow("Colorframe",frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):   #press to exit
            break
    else:
        break

cap2.release()
output.release()
cv2.destroyAllWindows()















