from state.gate import Gate

try:
    gate = Gate()
    gate.pay()
    gate.pay_ok()
    gate.enter()
except Exception as e:
    print(e)