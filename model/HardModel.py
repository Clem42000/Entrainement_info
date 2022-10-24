from contract.IModel import IModel


class HardModel(IModel):
    __helloWorld: str
    __title : str

    def __init__(self):
        self.__helloWorld = "helloworld"
        self.__title = "je me présente, je m'appelle Henry"

    def getHelloWorld(self) -> str:
        return self.__helloWorld

    def getTitle(self) -> str:
        return self.__title
