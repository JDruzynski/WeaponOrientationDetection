import cv2 as cv
import numpy as np
import os



def cannifyDir(inputDirectory:str, outputDirectory:str):
    if not os.path.isdir(outputDirectory): os.mkdir(outputDirectory)

    for filename in os.listdir(inputDirectory):
        if filename.endswith(".jpg"):
            im = cv.imread(os.path.join(inputDirectory, filename))
            im =cv.cvtColor(im, cv.COLOR_RGB2GRAY)
            im=cv.GaussianBlur(im, (5,5), 0)
            im=cv.Canny(im,50,150)

            cv.imwrite(os.path.join(outputDirectory, filename), im)

def getImages(directory:str)->list:
    return [cv.imread(os.path.join(directory, filename)) for filename in os.listdir(directory) if filename.endswith(".jpg")]


