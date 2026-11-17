from abc import ABC, abstractmethod

class InterFace_Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
