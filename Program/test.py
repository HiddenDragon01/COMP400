#!/usr/bin/env python
# coding: utf-8


# Name: Ryan Sowa
# ID: 260886668
# Prometheus Vision Facial Recognition Project


# This is the test file. As a chess player, I thought it would be interesting to 
# use famous chess players in my program. Here, I am counting the number of faces
# in the 'identify' directory and then, I am trying to recognize each of these 
# faces after initializing the training data set



import draw_box
import recognition_tools
import os


# First count the number of faces in each face in 'identify' and then print the number 
recognition_tools.number_faces('identify')

#Then, initialize the images in the training set
draw_box.init('training_set')


# Finally, for each photo in the 'identify' directory, draw a box around each recognized
# face with the name of that chess player
for file in os.listdir('identify'):
       draw_box.draw_box(os.path.join('identify', file))


