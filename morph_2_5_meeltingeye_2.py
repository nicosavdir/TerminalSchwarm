import time
import random
import os
clear = lambda: os.system('clear') #on Linux System


def Bubble(A,n):
    c=0
    sorted= True
    for i in range (0,n-1):
        if(A[i]>A[i+1]):
            c=A[i]
            A[i]=A[i+1]
            A[i+1]=c

            return False
    return sorted
'''
def Bubble2(A,n):
    i=0
    c=0
    sorted= True
    for i in range (0,n-1):
        if(A[i]>A[i+1]):
            c=A[i]
            A[i]=A[i+1]
            A[i+1]=c

            sorted = False
    time.sleep(0.03)
'''

def readimage(input,img):
    from PIL import Image
    from math import sqrt
    imag = Image.open(input)
    #Convert the image te RGB if it is a .gif for example
    imag = imag.convert ('RGB')
    #coordinates of the pixel
    #Get RGB

    for rows in range(size):
        for j in range(size):
            pixelRGB = imag.getpixel((j,rows))
            R,G,B = pixelRGB
            brightness = sum([R,G,B])/3 ##0 is dark (black) and 255 is bright (white)
            changepixel(j,rows,brightness*len(ascitable)/255,img)


def init(size):
    for i in range(size*size):
        pixels.append(0)
        pixels2.append(0)

def changepixel(x,y,brightness,img):
    if img==1:
        pixels[x-1+(y*size-size)]=int(brightness)
        return pixels
    else :
        pixels2[x-1+(y*size-size)]=int(brightness)
        return pixels2

def switchpixel1d(x,y,img):
    print("switching pix:"+str(x)+" with pix:"+str(y))
    #switching x with y
    tmp = int(pixels[x])
    if x != None:
        if img == 1:
            print(pixels[x])
            print(pixels[y])
            print("switch")
            pixels[x]=int(pixels[y])
            pixels[y]=tmp
            print(pixels[x])
            print(pixels[y])
            return pixels
        elif img == 2:
            pixels[x]=int(pixels[y])
            pixels[y]=tmp

def changepixel1d(x,brightness,img):
    print("changed pixel "+str(x)+" to brightness "+str(brightness))
    if x != None:
        if img == 1:
            pixels[x]=int(brightness)
            return pixels
        elif img == 2:
            pixels2[x]=int(brightness)
            return pixels2

def screen(pix):
    for rows in range(size):
        for i in range (size):
            ascii = pix[i+rows*size]
            if ascii >= len(ascitable): ascii -=1
            print(ascitable[ascii]+' ', end='')
        print(end='\n')

def countshades(pix):
    shades = []
    for i in range (len(ascitable)+2):
        val = 0
        for j in range(len(pix)):
            if pix[j]==i:
                val += 1
        shades.append(val)
        val =0
    return shades

def searchshade(pix,goal,type,recdepth):
    #Rev == reverese!
    i=random.randint(0,len(pix)-1)
    #print("searching for shade "+str(goal)+" /"+type+"/ looking at pixel "+str(i)+" its shade is "+str(pix[i]))
    #print(shadebal1)
    #print(shadebal2)
    if type == "nor":
        for j in range (50):
            if i+50 > len(pix):
                i-=50
            if pix[i+j]==goal:
                return int(i+j)
    elif type == "rev":
        if pix[i] != goal:
            return int(i)
    elif type == "bigger":
        if recdepth>20:
            for j in range(len(pix)):
                if pix[j] > goal:
                    return int(j)
        if pix[i] > goal:
            return int(i)
    elif type == "smaller":
        if pix[i] < goal:
            return int(i)

    return searchshade(pix,goal,type,recdepth+1)

def balanceshade(shade):
    time.sleep(0.15)
    clear()
    screen(pixels)
    #print(countshades(pixels))
    #print(countshades(pixels2))
    diff=abs(shadebal1[shade]-shadebal2[shade])
    for j in range(diff):
        if shadebal1[shade]<shadebal2[shade]:
            #print("< "+str(shade)+" "+ str(abs(shadebal1[shade]-shadebal2[shade])))
            p=searchshade(pixels,shade,"bigger",0)
            changepixel1d(p,shade,1)
            shadebal1[pixels[p]]-=1
            shadebal1[shade]+=1
        elif shadebal1[shade]>shadebal2[shade]:
            #print("> "+str(shade)+" "+ str(abs(shadebal1[shade]-shadebal2[shade])))
            p=searchshade(pixels,shade,"nor",0)
            changepixel1d(p,shade+1,1)
            shadebal1[shade]-=1
            shadebal1[shade+1]+=1
    return True

#searches in line
def resort1(resultpix):
    for i in range(len(pixels)):
        if pixels[i]!=resultpix[i]:
            for j in range(len(pixels)-i):
                if pixels[i+j]==resultpix[i]:
                    switchpixel1d(i,i+j,1)
                    return False
        if i == len(pixels):
            return True

#searches in line compares random
def resort2(resultpix):
    for i in range(len(pixels)):
        if pixels[i]!=resultpix[i]:
            for j in range(len(pixels)-i):
                r=random.randint(0,len(pixels)-1)
                if pixels[r]==resultpix[i]:
                    switchpixel1d(i,r,1)
                    return False
        if i == len(pixels):
            return True

#random
def resort3(resultpix):
    for i in range(len(pixels)):
        r=random.randint(0,len(pixels)-1)
        if pixels[r]!=resultpix[r]:
            for j in range(len(pixels)-r):
                if pixels[r+j]==resultpix[r]:
                    switchpixel1d(r,r+j,1)
                    return False
        if i == len(pixels):
            return True




for run in range(5):
    time.sleep(1)

    #INIT
    pixels=[]
    pixels2=[]
    shadebal1=[]
    shadebal2=[]
    size = 10
    ascitable=[' ','.','-',':','=','#','@','░','▒','■','▓','█']


    init(size)

    #Load Images
    readimage("input.jpg",1)
    readimage("inputv2.jpg",2)
    screen(pixels)
    time.sleep(1)

    #calculate shade balances
    shadebal1=countshades(pixels)
    shadebal2=countshades(pixels2)

    #Tune shade distribution
    for shd in range(len(ascitable)):
        while balanceshade(shd)== False:
            print()
        shadebal1=(countshades(pixels))
        shadebal2=(countshades(pixels2))

    time.sleep(1)
    screen(pixels)

    #Resort Image to Img2
    while resort1(pixels2)== False:
        clear()
        screen(pixels)

    #Sort all Pixels
    sorted=False
    while Bubble(pixels,len(pixels))==False:
        print('\33[5m'+"Bubbles0rt"+ '\033[0m')
        clear()
        screen(pixels)

    #RUN2
    print("run2##")
    time.sleep(0.5)
    readimage("input.jpg",2)

    #calculate shade balances
    shadebal1=countshades(pixels)
    shadebal2=countshades(pixels2)

    #Tune shade distribution
    for shd in range(len(ascitable)):
        while balanceshade(shd)== False:
            print()
        shadebal1=(countshades(pixels))
        shadebal2=(countshades(pixels2))

    time.sleep(1)
    screen(pixels)

    #Resort Image to Img2
    while resort1(pixels2)== False:
        clear()
        screen(pixels)
