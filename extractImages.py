#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: extractImages.py
    Author: Abel Moyo
    Date created: 08/10/2018
    Date last modified: 08/10/2018
    Python Version: 2.7
    Description: script that extracts images from a video file using openCV
"""
from argparse import ArgumentParser
from tqdm import tqdm
import cv2
import os
import time

def setupArgs():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="fileName",
                        help="input video file name", metavar="FILE")

    parser.add_argument("-d", "--directory", dest="destDir", default=".",
                        help="destination directory where the images are dropped, default is" 
                        " current directory", metavar="DIRECTORY")

    parser.add_argument("-e", "--extension", dest="extension", default="jpg",
                        help="type of image extension") 
                        
    parser.add_argument("-q", "--quiet", 
                        action="store_false", dest="verbose", default=True,
                        help="Dont' print status messages to stdout")

    return parser.parse_args()

def extractImages(args):

    capture = cv2.VideoCapture(args.fileName)
    destDir = args.destDir
    if not os.path.exists(destDir):
        os.makedirs(destDir)
    successfullRead, imageFile = capture.read()
    totalFrames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT)) 
    for frameNumber in tqdm(range(totalFrames)):
        if successfullRead:
            cv2.imwrite(("{0}/frame{1}.{2}".format(destDir, frameNumber, args.extension)), imageFile) 
        successfullRead, imageFile = capture.read()

args = setupArgs()
extractImages(args)