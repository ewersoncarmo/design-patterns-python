from abc import ABC, abstractmethod


class GateState(ABC):

    @abstractmethod
    def enter(self) -> None:
        pass

    @abstractmethod
    def pay(self) -> None:
        pass

    @abstractmethod
    def pay_ok(self) -> None:
        pass

    @abstractmethod
    def pay_fail(self) -> None:
        pass