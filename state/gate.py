from dataclasses import dataclass, field

from state.gate_state import GateState


@dataclass
class Gate():
    _gate_state: GateState = field(init=False)

    def __post_init__(self) -> None:
        from state.closed_gate_state import ClosedGateState

        self._gate_state = ClosedGateState(self)

    def change_state(self, state: GateState) -> None:
        self._gate_state = state

    def enter(self) -> None:
        self._gate_state.enter()

    def pay(self) -> None:
        self._gate_state.pay()

    def pay_ok(self) -> None:
        self._gate_state.pay_ok()

    def pay_fail(self) -> None:
        self._gate_state.pay_fail()