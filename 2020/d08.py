"""
Day 08 - boot loader

This puzzle defines a simple machine language for us to interpret and run.

The RealPython article says a [dataclass](https://docs.python.org/3/library/dataclasses.html) helps
to make a simple state machine. See [rp_state_machine.py](../misc/rp_state_machine.py)

Maybe a similar machine will be handy here.
"""

from dataclasses import dataclass
from os import stat
from typing import Dict, List, Set

@dataclass
class StateMachine:
    memory: Dict[str, int]
    program: List[str]
    instruction_history: List[int] = None

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


if __name__ == "__main__":

    with open('d08.input', 'r') as f:
        program: List[str] = f.readlines()
    
    state_machine: StateMachine = StateMachine(
        program=program,
        memory={'accumulator': 0}
    )

    try:
        state_machine.run()
    except Exception as e:
        print(e)
        print(f"[Part 1] Accumulator value: {state_machine.memory['accumulator']}")
    