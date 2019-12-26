import time

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
    print(shades)
    return shades

def seachshade(pix,goal):
    for i in range(len(pix)):
        if pix[i]==goal:
            return int(i)

def balanceshades(bal1,bal2):
    for i in range (len(ascitable)):
        if bal1!=bal2:
            if bal1[i]<bal2[i]:
                for j in range (bal2[i]-bal1[i]):
                    #print("dasas")
                    changepixel1d(seachshade(pixels,i+1),i,1)
            if bal1[i]>=bal2[i]:
                for j in range (bal1[i]-bal2[i]):
                    #print("dasas222")
                    changepixel1d(seachshade(pixels,i),i+1,1)
            print("--")
            print(countshades(pixels))
            print(countshades(pixels2))



pixels=[]
pixels2=[]
size = 42
ascitable=[' ','.','-',':','=','#','@','░','▒','■','▓','█']




init(size)
#pixels=changepixel(pixels,3,1,5)
#pixels=changepixel(pixels,3,3,9)
readimage("input.jpg",1)
readimage("inputv2.jpg",2)

#screen(pixels)
#print(pixels2)


balanceshades(countshades(pixels),countshades(pixels2))

#screen(pixels)

countshades(pixels)
countshades(pixels2)




sorted=False
'''while sorted==False:
    Bubble(pixels,len(pixels))
    screen(pixels)

print(readimage())'''
