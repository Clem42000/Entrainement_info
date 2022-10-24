from contract.IModel import IModel


class HardModel(IModel):
    __helloWorld: str

    def __init__(self):
        self.__helloWorld = "helloworld"

    def getHelloWorld(self) -> str:
        return self.__helloWorld
