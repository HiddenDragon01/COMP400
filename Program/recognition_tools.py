#!/usr/bin/env python
# coding: utf-8


# Name: Ryan Sowa
# ID: 260886668
# Prometheus Vision Facial Recognition Project


# Provide functionality to count the number of faces in a picture,
# count the number of faces for each picture in a given directory,
# and compare two images which have already been processed




import face_recognition
import os


# Count the number of faces in a given file. First, load the image, obtain an array of the locations
# of the faces, and then return the length of that array.
def num_faces(file):
    
    img = face_recognition.load_image_file(file)
    faces = face_recognition.face_locations(img)
    numfaces = len(faces)
    return numfaces




# Count the number of faces for each file in a given directory. Then, print the number of faces and the
# corresponding picture to the user
def number_faces(directory):
    
    for file in os.listdir(directory):
       numfaces = num_faces(os.path.join(directory, file))

       strfaces = "faces"

       if numfaces == 1:
        strfaces = "face"

       print(file , "contained" , numfaces , strfaces)




 # Compare two processed faces. Return the (boolean) comparison.
def compare_faces(processed1, processed2):
    
    comparison = face_recognition.compare_faces(processed1, processed2)
    return comparison


