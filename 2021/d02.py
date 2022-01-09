"""
Day 02 - Dive!

I solved [2020 Day 08](../2020/d08.py) with a StateMachine similar to the one
in the RealPython article (see [README](../README.md))

This is a very similar problem, so I'll use a similar machine.
(Maybe at some point, I'll make a machine where you can load in
the instruction set as well as the program!)

Part Two (of course!) uses a different instruction set. For now, it's easier
to just make a new state machine. Or add a 2nd run method...
"""

from dataclasses import dataclass
from typing import Dict, List

# Type aliases
Memory = Dict[str, int]
Program = List[str]


@dataclass
class StateMachine:
    memory: Memory
    program: Program

    def run(self):
        ip: int = 0  # instruction pointer

        instruction: str
        argument: str
        while ip < len(self.program):
            instruction, argument = self.program[ip].split(' ')

            # Machine implements 3 instructions
            if instruction == 'forward':
                self.memory['horizontal'] += int(argument)
            elif instruction == 'down':
                self.memory['depth'] += int(argument)
            elif instruction == 'up':
                self.memory['depth'] -= int(argument)
            else:
                raise Exception(f"Unknown instruction '{instruction} {argument}'.")
            ip += 1  # advance the instruction pointer
        return 0   # successful program run

    def run2(self):
        ip: int = 0  # instruction pointer

        instruction: str
        argument: str
        while ip < len(self.program):
            instruction, argument = self.program[ip].split(' ')

            # Machine implements 3 instructions
            if instruction == 'forward':
                self.memory['horizontal'] += int(argument)
                self.memory['depth'] += self.memory['aim'] * int(argument)
            elif instruction == 'down':
                self.memory['aim'] += int(argument)
            elif instruction == 'up':
                self.memory['aim'] -= int(argument)
            else:
                raise Exception(f"Unknown instruction '{instruction} {argument}'.")
            ip += 1  # advance the instruction pointer
        return 0   # successful program run


def solve_part1(program: Program) -> int:
    state_machine: StateMachine = StateMachine(
        program=program,
        memory={'horizontal': 0, 'depth': 0}
    )
    rc: int = state_machine.run()
    return state_machine.memory['horizontal'] * state_machine.memory['depth']


def solve_part2(program: Program) -> int:
    state_machine: StateMachine = StateMachine(
        program=program,
        memory={'horizontal': 0, 'depth': 0, 'aim': 0}
    )
    rc: int = state_machine.run2()
    return state_machine.memory['horizontal'] * state_machine.memory['depth']


if __name__ == "__main__":
    with open('d02.input', 'r') as f:
        program: Program = f.readlines()

    print(f"[Part 1] Our position*depth is {solve_part1(program)}.")
    print(f"[Part 2] Using 'aim', our position*depth is now {solve_part2(program)}.")
