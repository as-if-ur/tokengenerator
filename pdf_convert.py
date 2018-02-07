#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      saef
#
# Created:     01/12/2016
# Copyright:   (c) saef 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from fpdf import FPDF
from PIL import Image

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("out") if isfile(join("out", f))]

print onlyfiles
