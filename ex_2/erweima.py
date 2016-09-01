#coding:UTF-8

import Image,ImageDraw,ImageFont,ImageFilter
import random

def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor1():
    return  (random.randint(32,127),random.randint(32,127),random.randint(32,127))

def rndChar():
    return chr(random.randint(65,90))

outputPath = "G:\\py_ex\\ex_2\\"
fontPath = "C:\\Windows\\Fonts\\"

outputFile = "out.jpg"
font = ImageFont.truetype(fontPath+"Arial.ttf",36)

width = 60*4
height = 60
im = Image.new('RGB',(width,height),(255,255,255))

draw = ImageDraw.Draw(im)
for i in range(width):
    for j in range(height):
        draw.point((i,j),rndColor())

for f in range(4):
    draw.text((60*f+10,10),rndChar(),rndColor1(),font)

im = im.filter(ImageFilter.BLUR)
im.save(outputPath+outputFile)
