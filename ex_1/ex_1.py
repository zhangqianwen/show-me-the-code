# coding:utf-8

import Image,ImageDraw,ImageFont
import sys



inputPath = "G:\\py_ex\\ex_1\\"
outputPath = "G:\\py_ex\\ex_1\\"
fontPath = "C:\\Windows\\Fonts\\"

inputFile = "test.jpeg"
outputFile = "out.jpeg"

im = Image.open(inputPath+inputFile,'r')
draw = ImageDraw.Draw(im)
fontSize = min(im.size)/4
fontobj = ImageFont.truetype(fontPath+"simkai.ttf",fontSize)
draw.text((im.size[0]-fontSize,0),u'技',font=fontobj,fill=(255,0,0))

im.save(outputPath+outputFile,'jpeg')