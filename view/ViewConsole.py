from contract.IView import IView


class ViewConsole(IView):
    def display(self, message: str):
        print(message)
