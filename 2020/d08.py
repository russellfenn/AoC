"""
Day 08 - boot loader

This puzzle defines a simple machine language for us to interpret and run.

The RealPython article says a [dataclass](https://docs.python.org/3/library/dataclasses.html) helps
to make a simple state machine. See [rp_state_machine.py](../misc/rp_state_machine.py)

Maybe a similar machine will be handy here.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Set
from copy import deepcopy


# Type aliases
Memory = Dict[str, int]
Program = List[str]
History = Optional[List[int]]

@dataclass
class StateMachine:
    memory: Memory
    program: Program
    instruction_history: History = None

    def run(self):
        self.instruction_history = list()
        ip: int = 0  # instruction pointer, at start of the program

        while ip < len(self.program):
            if ip in self.instruction_history:
                raise Exception(f'Infinite Loop Detected! Memory Dump: {self.memory}')
            self.instruction_history.append(ip)
            instruction, argument = self.program[ip].split(' ')
            # This machine implements 3 instructions
            if instruction == 'nop':
                ip += 1
            elif instruction == 'acc':
                self.memory['accumulator'] += int(argument)
                ip += 1
            elif instruction == 'jmp':
                ip += int(argument)
            else:
                raise Exception('Invalid instruction')
        return 0  # successful program run!


def solve_part1(program: Program) -> int:
    state_machine: StateMachine = StateMachine(
        program=program,
        memory={'accumulator': 0}
    )

    try:
        state_machine.run()
    except Exception as e:
        print(e)
    return state_machine.memory['accumulator']


def solve_part2(program: Program) -> int:
    """Iterate through the program, changing nop -> jmp and jmp -> nop
       (working on a copy so we only change one instruction at a time).
       Running the program will either cause an exception or exit with 0.
       When we exit with 0, we have corrected the fault.
    """
    for i in range(len(program)):
        patched_program: Program = deepcopy(program)
        if patched_program[i].startswith('nop'):
            patched_program[i] = patched_program[i].replace('nop', 'jmp')
        elif patched_program[i].startswith('jmp'):
            patched_program[i] = patched_program[i].replace('jmp', 'nop')
        else:
            continue

        # try the patched program
        state_machine: StateMachine
        state_machine = StateMachine(
            program=patched_program,
            memory={'accumulator': 0}
        )
        try:
            # if no exception, then our program worked
            rc: int = state_machine.run()
            return state_machine.memory['accumulator']
        except Exception as e:
            # didn't work this time, try again
            # print(f"Attempted Patch at offset {i} failed.")
            pass
        del state_machine


if __name__ == "__main__":

    with open('d08.input', 'r') as f:
        program: Program = f.readlines()
    
    print(f"[Part 1] Accumulator value: {solve_part1(program)}")
    print(f"[Part 2] Corrected code - Accumulator value: {solve_part2(program)}")

