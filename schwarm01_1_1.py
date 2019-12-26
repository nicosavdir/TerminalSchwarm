#letsgoschwarmverhalten
import time
import random
import os
clear = lambda: os.system('clear') #on Linux System

size=[100,60]
asciitable=[' ','.','-',':','=','#','@','░','▒','■','▓','█']




def changeGrid(x,y,ascii):
    grid[y+x*size[1]]=ascii
    return grid

def screen(grid):
    clear()
    for rows in range(size[1]):
        for cols in range (size[0]):
            ascii = grid[rows+cols*size[1]]
            #if ascii >= len(asciitable): ascii -=1
            print(asciitable[ascii], end=' ')
        print(end='\n')


def init():
    grid=[]
    for i in range(size[0]*size[1]):
        grid.append(1)
    return grid

def spawnhomies(num):
    homie=[]
    for numhomies in range(num):
        homie.append(Homie(numhomies,random.randint(0,0),random.randint(0,size[0])))
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
      print(str(self.x)+str(self.y))
      changeGrid(self.x,self.y,self.ascii)

  #def random_move(self):




grid=init()


spawnhomies(50)


screen(grid)
