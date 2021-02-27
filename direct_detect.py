import cv2


cam=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
while(1):
    ret,frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,4)
    
    for(x,y,w,h) in faces:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)
       cv2.rectangle(frame,(120,0),(480,480),(255,255,0),3)
       if x<120:
           print("sağa")
       elif y<120:
           print("yukarı")
       elif y>240:
           print("aşağı")
       elif x>320:
           print("sola")
#           cv2.putText(frame,'left',(10,500),cv2.FONT_ITALIC,(255,0,255),2,cv2.LINE_AA)
    cv2.imshow("Face Detection",frame)
    if cv2.waitKey(1) == 27: 
        
        break  # esc to quit
    
    
    
    

cv2.destroyAllWindows()
