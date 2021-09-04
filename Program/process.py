#!/usr/bin/env python
# coding: utf-8

# Name: Ryan Sowa
# ID: 260886668
# Prometheus Vision Facial Recognition Project

import face_recognition
import os

# In order to compare two images in the face_recognition module, we must first process the images.
# Here, we provide the ability to process a given face, process many faces, or process the names 
# of the individuals in the training set





# Process a given face from a file. First, load the image, then return the processed image.
def process_face(file):
    
    print(file)
    img = face_recognition.load_image_file(file)
    processed = face_recognition.face_encodings(img)[0]
    return processed




# Loop through the faces in a given directory and return an array containing 
# the processed images in that directory.
def process_faces(directory):
    
    processed_faces = []
    
    for file in os.listdir(directory):
        
        processed_faces.append(process_face(os.path.join(directory, file)))
        
    return processed_faces




# The names in the training set directory should be in "firstname_lastname" form. 
# Parse this to obtain the first and last names, and add it to the processed 
# names array which we return.

def process_names(directory):

    processed_names = []
    
    for file in os.listdir(directory):
        
        removed_extension = os.path.splitext(file)[0]
        no_underscore = removed_extension.replace("_", " ")
        upper = no_underscore.title()
        processed_names.append(upper)   
        
    return processed_names
