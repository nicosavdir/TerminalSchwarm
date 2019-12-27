#letsgoschwarmverhalten
import time
import random
import os
clear = lambda: os.system('clear') #on Linux System

size=[300,135]
asciitable=[' ','.','-',':','=','#','@','░','▒','■','▓','█']
homies=[]




def changeGrid(x,y,ascii):
    grid[y+x*size[1]]=ascii
    return grid

def cleanscreen(var):
    if var ==0:
        for i in range(size[0]*size[1]):
            grid[i]=1
    else:
        for i in range(size[0]*size[1]):
            if grid[i]<=6 and grid[i]>0:
                grid[i]-=1


def screen(grid):
    clear()

    for rows in range(0,size[1]):
        for cols in range (0,size[0]):
            ascii = grid[rows+cols*size[1]]
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
        homie.append(Homie(numhomies,random.randint(20,size[0]-1-20),random.randint(20,size[1]-1-20)))
    return homie

def drawhomies():
    for numhomies in range(len(homies)):
        homies[numhomies].draw()

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

  def random_move(self):
    #1 2 3
    #4 0 5
    #6 7 8
    dir = random.randint(1,8)

    if dir==1:
        self.x-=1
        self.y-=1
    elif dir==2:
        self.y-=1
    elif dir==3:
        self.x+=1
        self.y-=1
    elif dir==4:
        self.x-=1
    elif dir==6:
        self.x+=1
    elif dir==6:
        self.x-=1
        self.y+=1
    elif dir==7:
        self.y+=1
    elif dir==8:
        self.x+=1
        self.y+=1




grid=init()

homies=spawnhomies(50)
for loop in range(100):
    time.sleep(0.1)

    cleanscreen(1)
    drawhomies()
    for h in range(0,len(homies)):
        homies[h].random_move()
#changeGrid(5,5,0)

    screen(grid)
