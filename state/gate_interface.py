from typing import Protocol

from state.gate_state import GateState


class GateProtocol(Protocol):

    def change_state(self, state: GateState) -> None:
        pass