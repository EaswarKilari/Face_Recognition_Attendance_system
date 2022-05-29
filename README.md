# Face Recognition Attendance management

The project aims at tracking attendance of employees/students of specific organizations
smartly replacing the biometric and manual attendance taking methods


## Features

- Mark your presence in one click
- Confirms your presence with a note


## UI

![Screenshot (180)](https://user-images.githubusercontent.com/81870353/170874621-6ad8734a-18ca-4a2c-9f9e-33a1c3f392b9.png)


![Screenshot (181)](https://user-images.githubusercontent.com/81870353/170874752-fe631fc4-d96a-44d6-a25a-4f1440cd0028.png)


## Project Structure

![image](https://user-images.githubusercontent.com/81870353/170874904-1bf9b390-8f76-47f4-a31f-2a4a5a8ffe6d.png)

## Files Explaination

- In main folder
   - AttendanceProject.py is used for face recognition and marking attendance
   - app.py runs the server using flask
   - Attendance.csv stores attendace 
   - requirements.txt stores requirements to run the above project
- Trainingimages folder stores images of all registered employees
- templates folder stores html files for website
- static folder stores static files like .css and .jpg files
- 

## Used By

This project is used by:

- Educational Institutions
- Offices 
- Industries where manual attendance is complex
- Malls, Restaurants, Hotels, etc 

## Installation

First Download or Clone the Project on Your Local Machine.

To download the project from github press Download Zip


![image](https://user-images.githubusercontent.com/81870353/170876004-1a679df0-3353-4723-8135-3c84fba6622c.png)

or

You can clone the project with git bash.To clone the project using git bash first open the git bash and write the following code
```bash
  git clone https://github.com/EaswarKilari/Face_Recognition_Attendance_system.git
```

After download, Open the project using Pycharm or VSCODE. Then we have to create an python enviroment to run the program.

To create enviroment
First open the terminal or command line in the IDE.Then write the following code.
~~~
python -m venv env
~~~

Then activate the enviroment using the code below for windows.
~~~
.\env\Scripts\activate
~~~


Installing the packages

~~~
pip install cmake
pip install dlib
pip install Face-recognition
pip install numpy
pip install opencv-python
pip install pyttsx3
~~~
Make sure you had python and Flask

Now Run the app.py file. It starts the server and provides an url. Click on the url, you will be directed to the website

## What can be improved

- Add mark out presence feature so that we can determine Toatl worked hours of employee
- Send attendance report to mails after each month to the employees
- Login feature can be added so that employee can we his/her attendance report
- In admin login new employee register, Train images and view reports features can be added
- All images and attendance can be stored in a database

## Thank You



