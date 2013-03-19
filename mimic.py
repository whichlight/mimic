#!/usr/bin/python

from imgproc import *
import LPD8806
import datetime
from optparse import OptionParser

parser= OptionParser()
parser.add_option("-d", "--data", 
		help="write data to stdout",
		default=False)

(opts, args) = parser.parse_args()


print "Starting MIMIC..."
my_cam = Camera(320,240)
led = LPD8806.strand()

while True:
	my_img = my_cam.grabImage()
	red, green, blue = my_img[160, 120]
	led.fill(red, green, blue)
	led.update()
	if (opts.data):
		print "\t".join(map(str,
			[datetime.datetime.now(),
			red,green,blue]))
	
	
	
	
