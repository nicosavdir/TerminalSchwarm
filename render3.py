import time

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
    #time.sleep(0.03)

pixels=[]
size = 150
ascitable=[' ','.','-',':','=','#','@','░','▒','■','▓','█']


def readimage(input):
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
            changepixel(j,rows,brightness*len(ascitable)/255)


def init(size):
    for i in range(size*size):
        pixels.append(0)

def changepixel(x,y,brightness):
    pixels[x-1+(y*size-size)]=brightness
    return pixels


def screen(pixels):
    for rows in range(size):
        for i in range (size):
            print(ascitable[int(pixels[i+rows*size])]+' ', end='')
        print(end='\n')

init(size)
#pixels=changepixel(pixels,3,1,5)
#pixels=changepixel(pixels,3,3,9)
readimage("input2.jpg")
sorted=False
screen(pixels)
while sorted==False:
    Bubble(pixels,len(pixels))
    screen(pixels)

print(readimage())
