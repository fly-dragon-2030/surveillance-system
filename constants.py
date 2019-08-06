# -*- coding: utf-8 -*-
"""
Created on Sat May 26 00:24:47 2018

@author: stephen
"""

image_exts = ['.jpeg','.jpg','.png','.bmp']
video_exts = ['.mpg','.mpeg','.mp4','.avi','m4v']
labels = ['background',
          'aeroplane',
          'bicycle',
          'bird',
          'boat',
          'bottle',
          'bus',
          'car',
          'cat',
          'chair',
          'cow',
          'diningtable',
          'dog',
          'horse',
          'motorbike',
          'pedestrian',
          'pottedplant',
          'sheep',
          'sofa',
          'train',
          'tvmonitor']

left_margin = 0#20
top_margin = 0#20

label_height = 40
label_gap = 3
label_length = 180
label_lenght__ = 600
__top_margin__ = 4
__left_margin__ = 4

text_height = label_height - 2 * __top_margin__

text_color = (255,255,255)#(255, 0, 255)
bg_color = (0,0,255)#(68, 68, 58)
overtime_color = (0,0,0)
restricted_color = (0,255,255)
wrong_color = (255,255,0)
crossover_color = (200,0,200)

screen_size = (1200,680)
display_size = (500,500)
video_size =(1920,1080)

