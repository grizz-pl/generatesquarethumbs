#!/usr/bin/env python
# -*- coding: utf-8 -*-
#generate thumb im by grizz - Witek Firlej http://grizz.pl

__project__      = "generate thumb im"
__author__    = "Witold Firlej (http://grizz.pl)"
__license__   = "GPL"
__copyright__ = "Witold Firlej"

import glob
import os

THUMB_SIZE = 125

for infile in glob.glob("*.jpg"):
	outfile = infile[:-4] + "_thumb.jpg"
	cmd = "convert " + infile +" -thumbnail x" + str(THUMB_SIZE*2) + " -resize \'" + str(THUMB_SIZE*2) +"x<\' -resize 50% -gravity center -crop " + str(THUMB_SIZE) + "x" + str(THUMB_SIZE) + "+0+0 +repage -format jpg -quality 91 " + outfile
#	print cmd
	os.system(cmd)
