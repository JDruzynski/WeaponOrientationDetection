from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any



class NNBase(ABC):
    model: Any

    @abstractmethod
    def trainModel(self, xtrain, ytrain, args*, kwargs**):
        pass

    @abstractmethod
    def evaluateModel(self, xtrain, ytrain, args*, kwargs**):
        pass

    @abstractmethod
    def predict(self, xdata, args*, kwargs**):
        pass

    @abstractmethod
    def modelSummary(self):
        pass

    @abstractmethod
    def saveModel(self, filename:str):
        pass

    @classmethod
    @abstractmethod
    def loadNet(cls, filename:str):
        pass







