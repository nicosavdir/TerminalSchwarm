#letsgoschwarmverhalten
import time
import random
import os
clear = lambda: os.system('clear') #on Linux System

size=[100,60]
asciitable=[' ','.','-',':','=','#','@','░','▒','■','▓','█']




def changeGrid(x,y,ascii):
    grid[x+y*size[0]]=ascii
    return grid

def screen(grid):
    clear()
    for rows in range(0,size[1]):
        for cols in range (0,size[0]):
            ascii = grid[cols+rows*size[0]]
            #if ascii >= len(asciitable): ascii -=1
            print(asciitable[ascii], end=' ')
            #print(ascii, end=' ')
        print(end='\n')


def init():
    grid=[]
    for i in range(size[0]*size[1]):
        grid.append(1)
    return grid

def spawnhomies(num):
    homie=[]
    for numhomies in range(num):
        homie.append(Homie(numhomies,random.randint(0,size[0]-1),random.randint(0,size[1]-1)))
        homie[numhomies].draw()
    return homie

class Homie :
  def __init__(self, id, x, y):
    self.x = x
    self.y = y
    self.id = id
    self.ascii = 6

  def myFunc(self):
    print("Hello my name is " + self.name)

  def draw(self):
      changeGrid(self.x,self.y,self.ascii)

  #def random_move(self):




grid=init()


spawnhomies(50)
#changeGrid(5,5,0)


screen(grid)
