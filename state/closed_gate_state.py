from dataclasses import dataclass

from state.gate_interface import GateProtocol
from state.gate_state import GateState


@dataclass
class ClosedGateState(GateState):
    _gate: GateProtocol

    def enter(self) -> None:
        raise Exception('The gate is closed. You need to pay first')

    def pay(self) -> None:
        from state.processing_gate_state import ProcessingGateState

        print('Processing payment')
        self._gate.change_state(ProcessingGateState(self._gate))

    def pay_ok(self) -> None:
        from state.open_gate_state import OpenGateState

        print('Payment ok')
        self._gate.change_state(OpenGateState(self._gate))

    def pay_fail(self) -> None:
        raise Exception('Payment failed')