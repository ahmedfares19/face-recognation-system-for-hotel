import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import cv2
import os
cap = cv2.VideoCapture(0)
i = 1
FaceObjectClassifier = cv2.CascadeClassifier(os.path.join("Classifiers" , "FaceDetection.xml" ))
classifier  = cv2.face.createLBPHFaceRecognizer()
classifier.load(os.path.join(os.getcwd() , "facesModels" , "shalan.xml" ))
counter = 0
name = ' '
font = cv2.FONT_HERSHEY_SIMPLEX
while cap.isOpened():
    suc , image = cap.read()
    counter += 1
    gray = cv2.cvtColor( image , cv2.COLOR_BGR2GRAY)
    faces = FaceObjectClassifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(80, 80))
    for x,y,w,h in faces:
        cv2.rectangle(image , (x,y) ,(x+w , y+h) ,(251, 251, 251) , 2)
        subImage = gray[y:y + h, x:x + w]
        resizedImage = cv2.resize(subImage, (168, 192))
        idx = classifier.predict(resizedImage)
        print  idx
        # if idx == 16:
        #     name = "Ahmed Fares"
        #     print name, idx
        # elif idx == 23:
        #     name = "ahmed salem"
        #     print name, idx
        # elif idx == 25:
        #     name = "mohamed shaalan"
        #     print name, idx
        # else:
        #     name = "Unkown"
        #     print name, idx


        cv2.putText(image, name, (x-2, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (250, 250, 250),2)


    cv2.imshow("Door", image)
    key = cv2.waitKey(1000 / 30)
    if key == 27 :
        break
cv2.destroyAllWindows()
cap.release()
