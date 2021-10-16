#import tensorflow as tf
#from tensorflow import keras
import numpy as np
from ImageOperations import cannifyDir



def main():
    dir1 = "D:\\GunDatasets\\OD-WeaponDetection\\Pistol detection\\Weapons"
    dir2 = "D:\\GunDatasets\\OD-WeaponDetection\\Pistol detection\\WeaponsCannified"

    cannifyDir(dir1, dir2)
    #Take all pictures from Subdir and generate new cannied dir

if __name__=="__main__":
    main()
