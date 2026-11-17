from abc import ABC, abstractmethod


class AICommand(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass
