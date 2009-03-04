#!/usr/bin/env python
# -*- coding: utf-8 -*-
#generate thumb pil by grizz - Witek Firlej http://grizz.pl

__project__      = "generate thumb pil"
__author__    = "Witold Firlej (http://grizz.pl)"
__license__   = "GPL"
__copyright__ = "Witold Firlej"

import glob
import Image

THUMB_SIZE = 125, 125

for infile in glob.glob("*.jpg"):
	img = Image.open(infile)
	width, height = img.size

	if width > height:
		delta = width - height
		left = int(delta/2)
		upper = 0
		right = height + left
		lower = height
	else:
		delta = height - width
		left = 0
		upper = int(delta/2)
		right = width
		lower = width + upper

	img = img.crop((left, upper, right, lower))
	img.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
	outfile = infile[:-4] + "_thumb.jpg"
	#print infile + " ==> " + outfile
	img.save(outfile, "JPEG")

