pixels=[]
size = 10
ascitable=[' ','.',':','-','=','@','#','░','▒','▓']

def init(size):
    for i in range(size*size):
        pixels.append(0)

def changepixel(pixels,x,y,brightness):
    pixels[x-1+(y*size-size)]=brightness
    return pixels


def screen(pixels):
    for rows in range(size):
        for i in range (size):
            print(ascitable[pixels[i+rows*size]], end='')
        print(end='\n')

init(size)
pixels=changepixel(pixels,3,1,5)
pixels=changepixel(pixels,3,3,9)
screen(pixels)
