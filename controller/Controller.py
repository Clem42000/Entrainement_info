from contract import IController
from contract import IView
from contract import IModel


class Controller(IController):
    __view: IView
    __model: IModel

    def __init__(self, view: IView, model: IModel):
        IController.__init__(self)
        self.__view = view
        self.__model = model

    def getView(self):
        return self.__view

    def getModel(self):
        return self.__model

    def start(self):
        self.__view(self.__model.getHelloWorld())
