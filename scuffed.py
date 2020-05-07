#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:43:45 2020

@author: garethlomax
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('bgnd2.jpg')


#route should be this form
route = np.array([[11,1], [10,5], [6, 6]])
two_starts = True
feet_follow_hands = True

def grid_to_graph_coord(route):
    route[:,0] = 11 - route[:,0] #flip
    return route

def route_coords(route):
    img_len = img.shape[0]
    offset = int((10/240) * img_len)
    spacing = int((20/240) * img_len)
    route *= spacing 
    route += offset
    return route

def plot_lines():
    square = True
    # wall_dim = 240
    wall_dim = img.shape[0]
    x = [0,wall_dim,wall_dim,0,0]
    y = [wall_dim,wall_dim,0,0,wall_dim]
    plt.plot(x,y)
    
if __name__ == "__main__":
    plt.figure()
    plt.imshow(img)
    plot_lines()
    # route = grid_to_graph_coord(route)
    
    route = route_coords(route)
    colors = np.zeros(len(route))
    colors[0] = 1
    if two_starts:
        colors[1] = 1
        print("bing")
    # colors = ['b', 'g','g']
    plt.scatter(route[:,1], route[:,0], c = colors)

    plt.plot(route[:,1], route[:,0])
    
    
    