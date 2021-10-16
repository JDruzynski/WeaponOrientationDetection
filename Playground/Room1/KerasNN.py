from NNBase import NNBase as Net


class KerasNN(Net):
    def trainModel(self, xtrain, ytrain, args*, kwargs**):
        self.model.fit(xtrain, ytrain, *args, **kwargs)

    def evaluateModel(self, xtrain, ytrain, args*, kwargs**):
        return self.model.evaluate(xtrain, ytrain, *args, **kwargs)

    def predict(self, xdata, args*, kwargs**):
        return self.model.predict(xdata, *args, **kwargs)

    def printModelSummary(self, args*, kwargs**):
        self.model.summary()

    def saveModel(self, filename:str, args*, kwargs**):
        pass

    @classmethod
    def loadNet(cls, filename:str, args*, kwargs**):
        pass


if __name__ == "__main__":
    pass
