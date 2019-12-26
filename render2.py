pixels=[]
size = 520
ascitable=[' ','.',':','-','=','@','#','░','▒','▓']

'''klauklau:'''
def readimage(input):
    from PIL import Image
    from math import sqrt
    imag = Image.open(input)
    #Convert the image te RGB if it is a .gif for example
    imag = imag.convert ('RGB')
    #coordinates of the pixel
    X,Y = 0,0
    #Get RGB

    for i in range(size):
        for j in range(size):
            pixelRGB = imag.getpixel((j,i))
            R,G,B = pixelRGB
            brightness = sum([R,G,B])/3 ##0 is dark (black) and 255 is bright (white)
            changepixel(j,i,brightness*len(ascitable)/255)


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
readimage("600.jpg")
screen(pixels)

print(readimage())
