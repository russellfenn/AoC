from d08 import StateMachine
import pytest
from typing import List

example_program_str = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

def test_part1_example():
    program: List[str] = example_program_str.splitlines()
    state_machine: StateMachine = StateMachine(
        program=program,
        memory={'accumulator': 0}
    )
    with pytest.raises(Exception):
        state_machine.run()
    assert state_machine.memory['accumulator'] == 5


fixed_example_program_str = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
nop -4
acc +6
"""

def test_part2_example():
    program: List[str] = fixed_example_program_str.splitlines()
    state_machine: StateMachine = StateMachine(
        program=program,
        memory={'accumulator': 0}
    )
    rc: int = state_machine.run()
    assert rc == 0
    assert state_machine.memory['accumulator'] == 8
