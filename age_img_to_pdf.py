from fpdf import FPDF
from PIL import Image
import glob
import os

print ('check')
# set here
image_directory = '/Users/algau/Desktop/virtage/age/'

#path = "/home/bunny/images/" # get the path of images

imagelist = os.listdir(image_directory) # get list of all images

pdf = FPDF('P','mm','A4') # create an A4-size pdf document

x,y,w,h = 0,0,200,250

for image in imagelist:

    pdf.add_page()
    pdf.image(image_directory+image,x,y,w,h)

pdf.output("images.pdf","F")
