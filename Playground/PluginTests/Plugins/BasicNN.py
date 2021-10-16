
from dataclasses import dataclass

import factory


@dataclass
class LoadedNN:
    file:str

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


def register() -> None:
    factory.register("LoadedNN", LoadedNN)
