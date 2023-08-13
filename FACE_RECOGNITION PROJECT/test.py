from sklearn.neighbors import KNeighborsClassifier
import sqlite3 as sq

conn=sq.connect("database/student.db")
cur=conn.cursor()

import cv2
import pickle
import numpy as np
import os


video=cv2.VideoCapture(0)
facedetect=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')



with open('data/names.pkl','rb') as f:
       LABEL=pickle.load(f)

with open('data/faces_data.pkl','rb') as f:
        FACES=pickle.load(f)

KNN=KNeighborsClassifier(n_neighbors=5)
KNN.fit(FACES,LABEL)


while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        crop_img=frame[y:y+h,x:x+w,:]
        resized_img=cv2.resize(crop_img,(50,50)).flatten().reshape(1,-1)
        output=KNN.predict(resized_img)       
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),1)
    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q') :
        break
video.release()
cv2.destroyAllWindows()

#print records
name=str(output)
index=(LABEL.index(output))/100+1
print(int(index))
cur.execute(f"select * from student_details where s_id={int(index)}")
row=cur.fetchall()
print("=================Student Details==================")
for record in row:
     print(f"Student Id:{record[0]}")
     print(f"Student First Name:{record[1]}")
     print(f"Student Middle Name:{record[2]}")
     print(f"Student Last Name:{record[3]}")
     print(f"Student Contact:{record[4]}")
     print(f"Student Exam Name:{record[5]}")
     print(f"Student Exam Mark:{record[6]}")