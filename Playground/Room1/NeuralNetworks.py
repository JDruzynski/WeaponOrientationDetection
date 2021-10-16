from KerasNN import KerasNN
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten

class KerasStruct1(KerasNN):
    model = Sequential(layers=[Conv2D()])
