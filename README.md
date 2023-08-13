 
# Face_Recognition Database

I developed a Python project in which I use the database and Face_Recognition.

This project is used to scan faces and add their entries to the database when we have to fetch any records we have to scan the face of that person then it returns all details of that person.

I used many Python libraries and use machine learning KNN algorithm to match faces.




## Installation

First of all clone the repo in your machine then install the required library.

```bash
pip install cv2
pip install pickle
pip install numpy 
pip install sqlite3 
pip install sklearn #for machine learning

```
Then run the add_faces.py first and enter data of the person or student then scan the face.

your entry into the database then you have to run test.py to scan faces and get in details of the person.

-> make .exe file of all program

Run the command to convert .py to .exe
-open cmd in the folder where your jarvis.py is located.

in cmd run the below command.

```bash
  pyinstaller <filename.py> --onefile
```  
Run .exe file
open dist then double click on jarvis your application starts running in cmd.

## Documentation

If you make your database for other use then you change the db.py file make your own table and insert feild.




