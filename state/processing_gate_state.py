from dataclasses import dataclass

from state.gate_interface import GateProtocol
from state.gate_state import GateState


@dataclass
class ProcessingGateState(GateState):
    _gate: GateProtocol

    def enter(self) -> None:
        raise Exception('Processing payment, please wait')

    def pay(self) -> None:
        raise Exception('Processing payment, please wait')

    def pay_ok(self) -> None:
        from state.open_gate_state import OpenGateState

        self._gate.change_state(OpenGateState(self._gate))

    def pay_fail(self) -> None:
        from state.closed_gate_state import ClosedGateState

        self._gate.change_state(ClosedGateState(self._gate))

