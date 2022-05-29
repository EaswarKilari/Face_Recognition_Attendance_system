import cv2
import numpy as np
import face_recognition
import os
import pyttsx3 as textSpeech
from datetime import datetime


engine = textSpeech.init()
path = 'Trainingimages'
images = []
classnames = []
mylist = os.listdir(path)
print(mylist)


#read all images in specified directory and append them in a list
#Considering name of image file as person name, append the names into names list
for cl in mylist:
    curImage = cv2.imread(f'{path}/{cl}')
    images.append(curImage)
    classnames.append(os.path.splitext(cl)[0])
print(classnames)


#find the encodings of all images (Training images)
def FindEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist


encodelistknown = FindEncodings(images)
print(len(encodelistknown))
print('Encoding completed')


#For noting attendance
#Take name as input and check whether the person attendance was already taken
#if attendance wasn't marked then add person's name and current time to .csv file
def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

            #Gives a voice message to let user know that his/her attendance is noted
            #statment = str('welcome ' + name)
            # engine.say(statment)
            # engine.runAndWait()
            # engine.endLoop()
            # engine.stop()


def take_attendance():
    #Capture image from webcam
    #we can also capture from screen(but avoided since we need live detection)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        success, img = cap.read()
        #Shorten the image and encode (original image may consume lot of time)
        imgs = cv2.resize(img,(0,0),None,0.25,0.25)
        imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

        #Find the all the faces in current frame and encode them
        facesCurFrame = face_recognition.face_locations(imgs)
        encodesCurFrame = face_recognition.face_encodings(imgs,facesCurFrame)
        flag=0

        #for each face in current frame scan with every other trained image and find the best match
        for encodeFace, faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodelistknown,encodeFace)
            faceDis = face_recognition.face_distance(encodelistknown, encodeFace)
            # print(faceDis)

            #find the image with least distance from current frame image
            matchIndex = np.argmin(faceDis)

            #To identify whether the current frame image is known
            if faceDis[matchIndex] < 0.50:
                name = classnames[matchIndex].upper()
                #markAttendance(name)
            else:
                name = "Unknown"
            print(name)

            #Find the face locations in current frame and label them with their name
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            #if name is known then mark his/her attendance
            if(name!="Unknown"):
                markAttendance(name)
                flag=1

        #Program automatically quits after noting attendance
        #If incace person is unidentified then press 'q' to quit
        cv2.imshow('Press ''q'' to quit', img)
        if cv2.waitKey(1) & 0xFF == ord('q') or flag==1 :
            break

    #Release all the holdings after execution
    cap.release()
    cv2.destroyAllWindows()

    #Returns name to print on the page
    return name