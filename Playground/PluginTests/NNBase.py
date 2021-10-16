from typing import Any, Protocol


class NNBase(Protocol):

    def createModel(self, *args, **kwargs):
        pass

    def trainModel(self, xtrain, ytrain, *args, **kwargs):
        pass

    def evaluateModel(self, xtrain, ytrain, *args, **kwargs):
        pass

    def predict(self, xdata, *args, **kwargs):
        pass

    def modelSummary(self):
        pass

    def saveModel(self, filename:str):
        pass







