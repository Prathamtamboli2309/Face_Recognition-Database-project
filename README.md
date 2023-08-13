 
# Face_Recognition Database

I developed a python project in which I use the database and Face_Recognition.

This project is used to scan faces and add their entries in database when we have to fetch any records we have to scan the face of that person then it returns all details of that person.

I used many python library and use machine learning KNN algorithm to match faces.




## Installation

First of all clone the repo in yout machine than install required library.

```bash
pip install cv2
pip install pickle
pip install numpy 
pip install sqlite3 
pip install sklearn #for machine learning

```
Then run the add_faces.py first and enter data of person or student then scan the face.

your entry into database then you have to run test.py to scan faces and get in details of person.

-> make .exe file of all program

Run command to convert .py to .exe
-open cmd in folder where you jarvis.py located.

in cmd run below command.

```bash
  pyinstaller <filename.py> --onefile
```  
Run .exe file
open dist then double click on jarvis your application is start running in cmd.

## Documentation

If you make your database for other use then you change db.py file make your own table and insert feild.




