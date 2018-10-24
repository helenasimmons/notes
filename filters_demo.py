from PIL import Image
from random import randint

img = Image.open("beach.jpg")
img.show() # original image

pixmap = img.load()

#for i in range(img.size[0]):
#    for j in range(img.size[1]):
#        r,g,b = pixmap[i,j]
#        
#        #r = randint(0,255)
#        g = randint(0,255)
#        #b = randint(0,255)
#        
#        pixmap[i,j] = (r,g,b)
        
def we_love_some_green(image):
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r,g,b = pixmap[i,j]
            r+= 20
            b += 20
            g = randint(100,255)
            
            pixmap[i,j] = (r,g,b)
            
    img.save("my_image.jpg")
    img.show()

def yeet(image):
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r,g,b = pixmap[i,j]
            
            r -= g
            g -= b
            b -= r
            
            pixmap[i,j] = (r, g, b)
    img.save("my_image.jpg")
    img.show()
yeet(img)
       
def slighty_more_green(image):
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r,g,b = pixmap[i,j]
            
            r += 25
            g += 50
            b += 25
            
            pixmap[i,j] = (r, g, b)
    img.save("my_image.jpg")
    img.show()

            
def phs_switch(image):
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r,g,b = pixmap[i,j]
            
            pixmap[i,j] = (g, b, r)
            
    img.show()
    

