from d02 import Memory, Program, StateMachine

example_program_str = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def test_part1_example():
    program: Program = example_program_str.splitlines()
    state_machine: StateMachine = StateMachine(
        program=program,
        memory={'horizontal': 0, 'depth': 0}
    )
    rc = state_machine.run()
    assert rc == 0
    assert state_machine.memory['depth'] == 10
    assert state_machine.memory['horizontal'] == 15


def test_part2_example():
    program: Program = example_program_str.splitlines()
    state_machine: StateMachine = StateMachine(
        program=program,
        memory={'horizontal': 0, 'depth': 0, 'aim': 0}
    )
    rc = state_machine.run2()
    assert rc == 0
    assert state_machine.memory['depth'] == 60
    assert state_machine.memory['horizontal'] == 15
