from contract.IView import IView


class ViewConsole(IView):
    __title : str

    def display(self, message: str):
        print("*"*40)
        print("* " + self.__title + " *")
        print("*"*40)
        print(message)

    def setTilte(self, title: str):
        self.__title = title
