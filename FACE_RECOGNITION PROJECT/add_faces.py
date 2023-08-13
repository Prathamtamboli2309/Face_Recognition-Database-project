import cv2
import pickle
import numpy as np
import os
import sqlite3 as sq;


conn=sq.connect("database/student.db")
cur=conn.cursor()


video=cv2.VideoCapture(0)
facedetect=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')


faces_data=[]


u_id_name={}
i=0

print("===================Enter Student Details=====================")
uni_id=int(input("Enter student id:"))
f_name=input("Enter Student First Name:")
m_name=input("Enter Student Middle Name:")
l_name=input("Enter Student Last Name:")
s_contact=int(input("Enter Student Contact:"))
exam_name=input("Enter Exam Name:")
exam_mark=int(input("Enter exam Marks:"))
row=(uni_id,f_name,m_name,l_name,s_contact,exam_name,exam_mark)
cur.execute("insert into student_details values(?,?,?,?,?,?,?)",row)
conn.commit()
conn.close()
u_id_name[uni_id]=f"{f_name}"
print(u_id_name)

while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        crop_img=frame[y:y+h,x:x+w,:]
        resized_img=cv2.resize(crop_img,(50,50))
        if len(faces_data)<=100 and i%10==0:
            faces_data.append(resized_img)
        i=i+1
        cv2.putText(frame,str(len(faces_data)),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(50,255,50),1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),1)
    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q') or len(faces_data)==100:
        break
video.release()
cv2.destroyAllWindows()

faces_data=np.asarray(faces_data)
faces_data=faces_data.reshape(100,-1)

if 'names.pkl' not in os.listdir('data/'):
    names=[f_name]*100
    with open('data/names.pkl','wb') as f:
        pickle.dump(names,f)
else:
    with open('data/names.pkl','rb') as f:
        names=pickle.load(f)
    names=names+[f_name]*100
    with open('data/names.pkl','wb') as f:
        pickle.dump(names,f)

if 'faces_data.pkl' not in os.listdir('data/'):
    
    with open('data/faces_data.pkl','wb') as f:
        pickle.dump(faces_data,f)
else:
    with open('data/faces_data.pkl','rb') as f:
        faces=pickle.load(f)
    faces=np.append(faces,faces_data,axis=0)
    with open('data/faces_data.pkl','wb') as f:
        pickle.dump(faces,f)









