from contract.IController import IController
from contract.IView import IView
from contract.IModel import IModel


class Controller(IController):
    __view: IView
    __model: IModel

    def __init__(self, view: IView, model: IModel):
        self.__view = view
        self.__model = model

    def getView(self):
        return self.__view

    def getModel(self):
        return self.__model

    def start(self):
        self.__view.display(self.__model.getHelloWorld())
