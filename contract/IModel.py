from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def getHelloWorld(self) -> str:
        ...

    def getTitle(self)->str:
        ...