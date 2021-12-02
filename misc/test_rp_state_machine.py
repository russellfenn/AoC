from rp_state_machine import StateMachine
from typing import Dict

def test_simple_program():
    state_machine: StateMachine = StateMachine(
        memory={"g": 0},
        program=["set g 44", "inc g"],
    )
    state_machine.run()
    assert state_machine.memory == {"g": 45}
