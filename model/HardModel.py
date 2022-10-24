from model import Model


class HardModel(Model):
    __helloWorld: str

    def __init__(self):
        Model.__init__(self)
        self.__helloWorld = "helloworld"

    def getHelloWorld(self) -> str:
        return self.__helloWorld
