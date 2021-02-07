from PIL import Image
import pyperclip
import numpy as np
from time import sleep

img = Image.open('')
img = img.resize((1200//20,1577//20))
pixels = img.load()
l = [[0]*img.size[1] for i in range(img.size[0])]

for i in range(img.size[0]):
    for j in range(img.size[1]):
        l[i][img.size[1]-j-1] = '#%02x%02x%02x' % pixels[i,j][:3]

def command(x,y):
    return "Calc.setExpression({latex:'("+str(x)+","+str(y)+")', color: '"+l[x][y]+"'})"

s = ''

for i in range(img.size[0]):
    for j in range(img.size[1]):
        s = s+command(i,j) + '\n'

pyperclip.copy(s)
