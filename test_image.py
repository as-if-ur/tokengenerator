#-------------------------------------------------------------------------------
# Name:        image writing test
# Purpose:
#
# Author:      saef
#
# Created:     30/11/2016
# Copyright:   (c) saef 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from fpdf import FPDF
import os
from os import listdir
from os.path import isfile, join

#from fpdf import FPDF
#from PIL import Image
import glob
#import os
import re



dir = os.path.dirname(__file__)

def tryint(s):
	try:
		return int(s)
	except:
		return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
	""" Sort the given list in the way that humans expect.
	"""
	l.sort(key=alphanum_key)

def makeImages(token_no_start,token_no_end,bg_file_name):
	font=ImageFont.truetype("arial.ttf", 48)
	# draw.text((x, y),"Sample Text",(r,g,b))
	pos_x=215
	pos_y=140
	#img.save('sample-out.jpg')
	ext=".jpg"
	for i in range(token_no_start,token_no_end+1):
		
		img = Image.open("in/"+bg_file_name)
		draw = ImageDraw.Draw(img)
		draw.text((pos_x, pos_y),str(i),(0,0,0),font=font)
		str_n=str(i)+ext
		img.save("out/"+str_n)
		#str_n=".png"
		print (str(i))
		i=i+1

def makePdf(pdfFileName):
	listPages = [f for f in listdir("out") if isfile(join("out", f))]
	sort_nicely(listPages)
	print listPages
	cover = Image.open("out/"+ str(listPages[0]))
	width, height = cover.size

	pdf = FPDF(unit = "pt", format = [width+80, height+30])
	pdf.add_page()
	for page in listPages:
		print "out/" + str(page)
		pdf.image("out/" + str(page))
	pdf.output( pdfFileName , "F")

makeImages(1,20,"S-2.png")
makePdf("S-2.pdf")