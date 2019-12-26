#letsgoschwarmverhalten
import time
import random
import os
clear = lambda: os.system('clear') #on Linux System

size=[100,60]
asciitable=[' ','.','-',':','=','#','@','░','▒','■','▓','█']



def screen(pix):
    clear()
    for rows in range(size[1]):
        for cols in range (size[0]):
            ascii = pix[cols+rows*size[0]]
            #if ascii >= len(asciitable): ascii -=1
            print(asciitable[ascii], end=' ')
        print(end='\n')


def init():
    grid=[]
    for i in range(size[0]*size[1]):
        grid.append(0)
    return grid


grid=init()
screen(grid)
