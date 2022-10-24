from abc import ABC

from contract import IView

class View (ABC,IView):
    def __init__(self):
        IView.__init__(self)