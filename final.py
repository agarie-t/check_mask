import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

mouth_cascade = cv2.CascadeClassifier('mouth.xml')

nose_cascade = cv2.CascadeClassifier('nose.xml')

cap = cv2.VideoCapture(0)

while(1):
    
    ret, frame = cap.read()

    height = frame.shape[0]

    width = frame.shape[1]
    
    face_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(face_gray)
    
    m=0
    n=0
    
    for (x,y,w,h) in faces:

        gray = face_gray[y:y+h, x:x+w]
        color = frame[y:y+h, x:x+w]
        
        mouth = mouth_cascade.detectMultiScale(gray)
        nose = nose_cascade.detectMultiScale(gray)
        
        m=0
        n=0
        
        for (mx,my,mw,mh) in mouth:
            m=1
            
        for (nx,ny,nw,nh) in nose:
            n=1
    
    if m==1 and n==1:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(frame, "No mask", (10, 460), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,255), 2)
    else:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    result= cv2.resize(frame,(width*2, height*2))

    cv2.imshow("RESULT", result)
    
    finish = [ord('f'), ord('F')]
    key = cv2.waitKey(100)
    
    if key in finish:
        break

cap.release()

cv2.destroyAllWindows()