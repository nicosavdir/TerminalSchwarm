import time
import random
import os
clear = lambda: os.system('clear') #on Linux System

'''
def Bubble(A,n):
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
            print(ascitable[pix[i+rows*size]]+' ', end='')
        print(end='\n')

def countshades(pix):
    shades = []
    for i in range (len(ascitable)):
        val = 0
        for j in range(len(pix)):
            if pix[j]==i:
                val += 1
        shades.append(val)
        val =0
    return shades

def searchshade(pix,goal,type):
    #Rev == reverese!
    i=random.randint(0,len(pix)-1)
    #print("searching for shade "+str(goal)+" /"+type+"/ looking at pixel "+str(i)+" its shade is "+str(pix[i]))
    if type == "nor":
        for j in range (50):    #man braucht das um die max. recursionstiefee nicht zu überschreiten
            if i+50 > len(pix): #
                i-=50           #
            if pix[i+j]==goal:
                return int(i+j)
    elif type == "rev":
        if pix[i] != goal:
            return int(i)
    elif type == "bigger":
        if pix[i] > goal:
            return int(i)
    elif type == "smaller":
        if pix[i] < goal:
            return int(i)

    return searchshade(pix,goal,type)

def balanceshade(shade):
    diff=abs(shadebal1[shade]-shadebal2[shade])
    for j in range(diff):
        clear()
        screen(pixels)
        if shadebal1[shade]<shadebal2[shade]:
            #print("< "+str(shade)+" "+ str(abs(shadebal1[shade]-shadebal2[shade])))
            p=searchshade(pixels,shade,"bigger")
            changepixel1d(p,shade,1)
            shadebal1[pixels[p]]-=1
            shadebal1[shade]+=1
        elif shadebal1[shade]>shadebal2[shade]:
            #print("> "+str(shade)+" "+ str(abs(shadebal1[shade]-shadebal2[shade])))
            p=searchshade(pixels,shade,"nor")
            changepixel1d(p,shade+1,1)
            shadebal1[shade]-=1
            shadebal1[shade+1]+=1
    return True








for run in range(1):
    time.sleep(0.5)


    pixels=[]
    pixels2=[]
    shadebal1=[]
    shadebal2=[]
    size = 42
    ascitable=[' ','.','-',':','=','#','@','░','▒','■','▓','█']

    init(size)
    #pixels=changepixel(pixels,3,1,5)
    #pixels=changepixel(pixels,3,3,9)
    readimage("input.jpg",1)
    readimage("inputv2.jpg",2)

    #screen(pixels)
    #print(pixels2)

    shadebal1=countshades(pixels)
    shadebal2=countshades(pixels2)

    for shd in range(len(ascitable)):
        while balanceshade(shd)== False:
            print()
        shadebal1=(countshades(pixels))
        shadebal2=(countshades(pixels2))
    screen(pixels)
    print(countshades(pixels))
    print(countshades(pixels2))
    print(shadebal1)
    print(shadebal2)




sorted=False
'''while sorted==False:
    Bubble(pixels,len(pixels))
    screen(pixels)

print(readimage())'''
