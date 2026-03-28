from dataclasses import dataclass

from state.gate_interface import GateProtocol
from state.gate_state import GateState


@dataclass
class OpenGateState(GateState):
    _gate: GateProtocol

    def enter(self) -> None:
        from state.closed_gate_state import ClosedGateState

        print('Entering gate')
        self._gate.change_state(ClosedGateState(self._gate))
        print('Closing gate')

    def pay(self) -> None:
        print('The gate is open')

    def pay_ok(self) -> None:
        print('The gate is open')

    def pay_fail(self) -> None:
        raise Exception('Payment failed')


