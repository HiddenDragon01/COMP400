#!/usr/bin/env python
# coding: utf-8


# Name: Ryan Sowa
# ID: 260886668
# Prometheus Vision Facial Recognition Project

# Provides functionality for initializing known_faces
# and known_names as well as drawing a box with a name
# around the faces of individuals who are recognized
# from the training set

import face_recognition
import recognition_tools
import process
from PIL import Image, ImageDraw



# Define known_faces, an array of known faces in the training set and 
# known_names, an array of the corresponding names with those faces.
known_faces = []
known_names = []




# Instantiate known_faces and known_names with the proper values given a directory. 
# This should only be done once given that the photos in the directory do not change.
def init(known_directory):
    
    print("Initializing...")
    global known_names, known_faces
    known_faces = process.process_faces(known_directory)
    known_names = process.process_names(known_directory)




# After calling init(), use the information we know about known faces and known names
# to draw boxes around recognized faces in a given image.
def draw_box(identify_file):
    
    # If init is not called yet, then print an error message and return an error.
    if not known_faces or not known_names:
        
        print("Not initialized yet!")
        return -1
    
    # Load the image file and process it.
    identify = face_recognition.load_image_file(identify_file)
    identify_coords = face_recognition.face_locations(identify)
    identify_processed = face_recognition.face_encodings(identify, identify_coords)
    
    # Prepare to draw boxes on the image.
    converted = Image.fromarray(identify)
    pil_img = ImageDraw.Draw(converted)
    
    for(y2, x2, y1, x1), processed in zip(identify_coords, identify_processed):
        
        # Make the comparison and set name by default to "Not Recognized". If there
        # is no match, then "Not Recognized" will be shown.
        identified = recognition_tools.compare_faces(processed, known_faces)
        name = "Not Recognized"
        
        # If there is a match, then save the first index and name of that match.
        if True in identified:
            index = identified.index(True)
            name = known_names[index]
        
        # Draw the rectangle with these parameters.
        pil_img.rectangle(((x1, y2), (x2, y1)), outline=(0,0,0))
        text_width, text_height = pil_img.textsize(name)
             
        pil_img.rectangle(((x1, y1 - text_height - 10), (x2, y1)), fill = (0,0,0), outline=(0,0,0))
        pil_img.text((x1 + 6, y1 - text_height - 5), name, fill=(255, 255, 255, 255))
        
    # Delete pil_img as a best practice.
    del pil_img
    
    # Display the image with the drawn rectangles.
    converted.show()
   