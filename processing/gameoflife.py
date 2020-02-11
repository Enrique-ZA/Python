# Conway's game of life in processing py
# Installation:
# Download - https://processing.org/download/
# Install processing
# Top right add mode python (Should be java by default)
# Switch mode to python

'''
# Conway's Game Of Life in Processing Py
# using python arrays
# Author: Enrique Nelson
# 62746405@mylife.unisa.ac.za
# https://github.com/Enrique-ZA
'''

from array import *

grid = array('i',[])
cols = 0
rows = 0
res = 10

def countNeighbours(grid, x, y):
    sum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            col = (x + i + cols) % cols
            row = (y + j + rows) % rows                        
            index = row * cols + col        
            sum += grid[index]
    index = y * cols + x
    sum -= grid[index]
    return sum
            

def setup():
    global grid, cols, rows, res
    
    size(600, 400)
    
    cols = width / res
    rows = height / res
    
    for i in range(cols): 
        for j in range(rows): 
            grid.append(int(floor(random(2))))
            
def draw():
    global grid, cols, rows, res
    background(0);
    
    for i in range(cols): 
        for j in range(rows):
            index = j * cols + i
            x = i * res
            y = j * res
            stroke(0)
            if(grid[index] == 1):
                fill(255)
            else:
                fill(0)
            rect(x, y, res, res)
            
    next = array('i',[])
    
    for i in range(cols): 
        for j in range(rows): 
            next.append(0)
    
    # Compute next based on grid
    
    for i in range(cols): 
        for j in range(rows):
            index = j * cols + i
            
            state = grid[index]
            
            # Count live neighbours
            neighbours = countNeighbours(grid, i, j)
            
            if(state == 0 and neighbours == 3):
                next[index] = 1
            elif(state == 1 and (neighbours < 2 or neighbours > 3)):
                next[index] = 0
            else:
                next[index] = state
    
    # Set grid equal to next
    for i in range(cols): 
        for j in range(rows):
            index = j * cols + i
            grid[index] = next[index]
