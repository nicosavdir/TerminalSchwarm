#letsgoschwarmverhalten
import time
import random
import os
clear = lambda: os.system('clear') #on Linux System

size=[100,65]
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
    for i in range(20):
        changeGrid(3*i,2*i,10)


def screen(grid):
    clear()

    for rows in range(0,size[1]):
        for cols in range (0,size[0]):
            ascii = grid[rows+cols*size[1]]
            #if ascii >= len(asciitable): ascii -=1
            print(asciitable[ascii], end=' ')
            #print(ascii, end=' ')
        print(end='\n')

def getGrid(x,y):
    return grid[y+x*size[1]]

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
        do = 0
        viewed=homies[numhomies].view()
        for v in range(len(viewed)):
            if viewed[v]==1:
                do = 0
            elif viewed[v]==10:
                do = 10

        if do == 0:
            homies[numhomies].random_move()
        elif do == 10:
            print("10!")
        homies[numhomies].draw()


class Homie :
  def __init__(self, id, x, y):
    self.x = x
    self.y = y
    self.id = id
    self.ascii = 6
    self.direction = random.randint(0,8)

  def myFunc(self):
    print("Hello my name is " + self.name)

  def draw(self):
      changeGrid(self.x,self.y,self.ascii)

  def random_move(self):
    #1 2 3
    #4 0 5
    #6 7 8
    dir = random.randint(0,8)

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


  def view(self):
      v_range=5
      viewarray=[]

      for rows in range(v_range):
          for cols in range(v_range):
              g1=int(self.x -2 +cols)
              g2=int(self.y -2 +rows)
              viewarray.append(getGrid(g1,g2))

              changeGrid(g1,g2,0)

      return viewarray






grid=init()

homies=spawnhomies(10)
while True:
    time.sleep(0.1)

    cleanscreen(0)
    drawhomies()

    screen(grid)
