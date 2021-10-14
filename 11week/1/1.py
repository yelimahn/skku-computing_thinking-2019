from PIL import Image
from PIL import ImageFilter

img=Image.open('road.png')

pix=img.load()

def min_select(r,g,b):
    if r<g:
        if r<b:
            #r min
            return r
        else:
            #b min
            return b
    else:
        if r<b:
            #g min
            return g
        elif g<b:
            #g min
            return g
        else:
            #b min
            return b

for i in range(430):

    for j in range(322):
        if i>300:
            pix[i,j]=(0,0,0,255)
        elif j<100:
            pix[i,j]=(0,0,0,255)
        else:
            r,g,b=img.getpixel((i,j))
            mini=min_select(r,g,b)
            #0xf0은 240
            if mini>=240:
                pix[i,j]=(255,255,255,255)
            else:
                pix[i,j]=(0,0,0,255)


image=img.filter(ImageFilter.FIND_EDGES)
image.show()
image.save('road_result.png')


