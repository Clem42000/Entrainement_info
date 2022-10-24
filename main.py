from controller.Controller import Controller
from model.HardModel import HardModel
from view.ViewConsole import ViewConsole

controller = Controller(ViewConsole(), HardModel())
controller.start()
