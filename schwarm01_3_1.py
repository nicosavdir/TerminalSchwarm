#letsgoschwarmverhalten
#IMPORTS________________________________________________________________________
import time
import random
import os
clear = lambda: os.system('clear') #on Linux System

size=[100,65]
asciitable=[' ','.','-',':','=','#','@','░','▒','■','▓','█']
homies=[]
obstacles=[]

#CLASSES________________________________________________________________________
class Homie :
  def __init__(self, id, x, y):
    self.x = x
    self.y = y
    self.id = id
    self.ascii = 6
    self.direction = random.randint(0,8)
    self.do = 0
    self.visionlen = 5

  def myFunc(self):
    print("Hello my name is " + self.name)

  def draw(self):
      #self.drawviewarea()
      changeGrid(self.x,self.y,self.ascii)

  def random_move(self):
    dir = random.randint(0,8)
    self.movedir(dir)

  def movedir(self,dir):
      #1 2 3
      #4 0 5
      #6 7 8
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

  def move_avoid(self,ascii):
      for rows in range(self.visionlen):
          for cols in range(self.visionlen):
              print("TODO")


  def view(self):
      viewarray=[]
      for rows in range(self.visionlen):
          for cols in range(self.visionlen):
              g1=int(self.x - int((self.visionlen-1)/2) +cols)
              g2=int(self.y - int((self.visionlen-1)/2) +rows)

              viewarray.append(getGrid(g1,g2))

              changeGrid(g1,g2,0)
      return viewarray

  def think(self):
      viewed=self.view()
      print(viewed)
      if viewed.__contains__(10):
          self.do=10

      if self.do == 0:
          self.random_move()
      elif self.do == 10:
          print("10!")


class Obstacle:
  def __init__(self, id, x, y, height, width, ascii):
    self.x = x
    self.y = y
    self.height = height
    self.width = width
    self.id = id
    self.ascii = 10

  def draw(self):
      for rows in range(self.height):
        for cols in range(self.width):
            changeGrid(self.x+cols,self.y+rows,self.ascii)


#FUNCTIONS______________________________________________________________________
def init():
    grid=[]
    for i in range(size[0]*size[1]):
        grid.append(1)
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
        print(end='\n')

def getGrid(x,y):
    return grid[y+x*size[1]]

def changeGrid(x,y,ascii):
    grid[y+x*size[1]]=ascii
    return grid

def spawnhomies(num):
    homie=[]
    for numhomies in range(num):
        homie.append(Homie(numhomies,random.randint(20,size[0]-1-20),random.randint(20,size[1]-1-20)))
    return homie

def iteratehomies(func):
    for numhomies in range(len(homies)):
        if func==0:
            homies[numhomies].think()
        elif func ==1:
            homies[numhomies].draw()


def spawnObstacles(num,ascii):
    for numObstacles in range(num):
        obsSize=[2,2]
        obstacles.append(Obstacle(numObstacles,random.randint(0,size[0]-1-obsSize[0]),random.randint(0,size[1]-1-obsSize[1]),obsSize[0],obsSize[1],ascii))
    return obstacles

def drawObstacles():
    for numObstacles in range(len(obstacles)):
        obstacles[numObstacles].draw()

#RUN____________________________________________________________________________
grid=init()

homies=spawnhomies(10)
obstacles=spawnObstacles(10,10)
while True:
    time.sleep(0.1)

    iteratehomies(0)#THINK
    cleanscreen(0)
    drawObstacles()
    iteratehomies(1)#DRAW

    screen(grid)


'''TRASHCAN

  def drawviewarea(self):
       viewarray=[]
       for rows in range(self.visionlen):
           for cols in range(self.visionlen):
               g1=int(self.x - int((visionlen-1)/2) +cols)
               g2=int(self.y - int((visionlen-1)/2) +rows)
               changeGrid(g1,g2,0)




'''
