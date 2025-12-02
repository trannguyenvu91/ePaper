#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in3e
from PIL import Image
from PhotoManager import getImagePathToDisplay

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("1. epd7in3f Demo")

    epd = epd7in3e.EPD()   
    logging.info("2. init and Clear")
    epd.init()
    epd.Clear()

    # read bmp file
    imageToDisplay = getImagePathToDisplay()
    logging.info(f"3. read bmp file: {imageToDisplay}")
    Himage = Image.open(imageToDisplay)
    epd.display(epd.getbuffer(Himage))
    
    logging.info("4. Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in3e.epdconfig.module_exit(cleanup=True)
    exit()
