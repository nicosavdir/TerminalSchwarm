#letsgoschwarmverhalten
#IMPORTS________________________________________________________________________
import time
import random
import os
import math
import numpy as np
clear = lambda: os.system('clear') #on Linux System

size=[100,65]
asciitable=[' ','.','-',':','=','#','@','░','▒','■','▓','█']
homies=[]
obstacles=[]
food = []

#CLASSES________________________________________________________________________
class Homie :
  def __init__(self, id, x, y):
    self.x = x
    self.y = y
    self.id = id
    self.ascii = 6
    self.direction = random.randint(0,8)
    self.do = 0
    self.visionlen = 7
    self.viewarray = []

  def myFunc(self):
    print("Hello my name is " + self.name)

  def draw(self):
      #self.drawviewarea()
      changeGrid(self.x,self.y,self.ascii)

  def random_move(self):
    dir = random.randint(0,8)
    self.movedir(dir)

  def movedir(self,dir):
      #7 0 1
      #6 8 2
      #5 4 3
      if dir==7:
          self.x-=1
          self.y-=1
      elif dir==0:
          self.y-=1
      elif dir==1:
          self.x+=1
          self.y-=1
      elif dir==6:
          self.x-=1
      elif dir==2:
          self.x+=1
      elif dir==5:
          self.x-=1
          self.y+=1
      elif dir==4:
          self.y+=1
      elif dir==3:
          self.x+=1
          self.y+=1

  def move_avoid(self,ascii):
      avoid_vectors = []
      for i in range(self.visionlen*self.visionlen):
          if self.viewarray[i]==ascii:
              avoid_vectors.append(self.calcViewVec(i,self.viewarray))

      addedvec=[0,0]
      for i in range(len(avoid_vectors)):
          addedvec=addVec(addedvec,avoid_vectors[i])

      self.movedir(vec2dir(invertVec(addedvec)))
      if addedvec==[0,0]:
          return True
      else: return False

      #schöner machen
  def move_Target(self,ascii):
      vectors = []
      for i in range(self.visionlen*self.visionlen):
          if self.viewarray[i]==ascii:
              vectors.append(self.calcViewVec(i,self.viewarray))

      addedvec=[0,0]
      for i in range(len(vectors)):
          addedvec=addVec(addedvec,vectors[i])

      self.movedir(vec2dir(addedvec))
      if addedvec==[0,0]:
          return True
      else: return False

  def eat(self):
      for i in range(len(food)-1):
        if self.x == food[i].x and self.y == food[i].y:
            print("essen")
            food.pop(i)

  def calcViewVec(self,i,viewarr):
      x=(i%self.visionlen)-int((self.visionlen-1)/2)
      y=(int((i-x)/self.visionlen))-int((self.visionlen-1)/2)
      return [x,y]


  def view(self):
      self.viewarray=[]
      for rows in range(self.visionlen):
          for cols in range(self.visionlen):
              g1=int(self.x - int((self.visionlen-1)/2) +cols)
              g2=int(self.y - int((self.visionlen-1)/2) +rows)

              self.viewarray.append(getGrid(g1,g2))

              changeGrid(g1,g2,0)
      return self.viewarray

  def think(self):
      viewed=self.view()
      if viewed.__contains__(10):
          self.do=10
      elif viewed.__contains__(1):
          self.do=1

      if self.do == 0:
          self.random_move()
      elif self.do == 10:
          if self.move_avoid(10):
              self.do=0
      elif self.do == 1:
          self.eat()
          if self.move_Target(1):
              self.eat()
              self.do=0



class Obstacle:
  def __init__(self, id, x, y, height, width, ascii):
    self.x = x
    self.y = y
    self.height = height
    self.width = width
    self.id = id
    self.ascii = ascii

  def draw(self):
      for rows in range(self.height):
        for cols in range(self.width):
            changeGrid(self.x+cols,self.y+rows,self.ascii)


#FUNCTIONS______________________________________________________________________
def init():
    grid=[]
    for i in range(size[0]*size[1]):
        grid.append(0)
    return grid

def cleanscreen(var):
    if var ==0:
        for i in range(size[0]*size[1]):
            grid[i]=0
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
    edge=5
    homie=[]
    for numhomies in range(num):
        homie.append(Homie(numhomies,random.randint(edge,size[0]-1-edge),random.randint(edge,size[1]-1-edge)))
    return homie

def iteratehomies(func):
    for numhomies in range(len(homies)):
        if func==0:
            homies[numhomies].think()
        elif func ==1:
            homies[numhomies].draw()

def spawnObstacles(num,ascii):
    for numObstacles in range(num):
        obsSize=[random.randint(0,10),random.randint(0,10)]
        obstacles.append(Obstacle(numObstacles,random.randint(0,size[0]-1-obsSize[0]),random.randint(0,size[1]-1-obsSize[1]),obsSize[0],obsSize[1],ascii))
    return obstacles

def spawnFood(num,ascii):
    for numObstacles in range(num):
        obsSize=[1,1]
        obstacles.append(Obstacle(numObstacles,random.randint(0,size[0]-1-obsSize[0]),random.randint(0,size[1]-1-obsSize[1]),obsSize[0],obsSize[1],ascii))
    return obstacles

def drawObstacles(obstacles):
    for numObstacles in range(len(obstacles)):
        obstacles[numObstacles].draw()

def buildWall():
    for i in range(2):
        for j in range(size[0]):
            changeGrid(j,0,10)
            changeGrid(j,size[1]-1,10)
        for j in range(size[1]):
            changeGrid(0,j,10)
            changeGrid(size[0]-1,j,10)

#Angelfunctions
def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def vec2dir(vec):
    base=[0,-1]
    v1_u = unit_vector(base)
    v2_u = unit_vector(vec)
    rad=math.degrees(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))
    if vec==[0,0]:
        return 8
    elif vec[0]<0:
        return int((360-rad)/45)
    else:
        return int(rad/45)

def addVec(vec1, vec2):
    vec=[0,0]
    vec[0]=vec1[0]+vec2[0]
    vec[1]=vec1[1]+vec2[1]
    return vec

def Vec2Length(vec):
    return abs(sqrt( (vec[0]*vec[0]) + (vec[1]*vec[1])))

def invertVec(vec): return[-vec[0],-vec[1]]


#RUN____________________________________________________________________________
grid=init()

homies=spawnhomies(50)
obstacles=spawnObstacles(20,10)
food=spawnFood(20,1)
while True:
    time.sleep(0.1)

    iteratehomies(0)#THINK
    cleanscreen(0)
    drawObstacles(obstacles)
    drawObstacles(food)
    buildWall()
    iteratehomies(1)#DRAW

    screen(grid)


'''TRASHCAN

'''
