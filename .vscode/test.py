from PIL import Image
import numpy as np
import sys

img = Image.open("C:\choun1.jpg")

size = str(img.size)

img = np.array(img)
img=img.tolist()
img=str(img)


characters = "[],"
for x in range(len(characters)):
    img = img.replace(characters[x],"")

img = img.split()
img=list(map(int,img))

characters = ",()"
for x in range(len(characters)):
    size = size.replace(characters[x],"")
size = size.split()
size = list(map(int,size))

img=np.array(img).reshape((size[1],size[0],3))
img2 = Image.fromarray(img, 'RGB')
img2.show()
