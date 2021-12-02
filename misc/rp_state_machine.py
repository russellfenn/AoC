"""
Real Python State Machine

The RP article on [AoC](https://realpython.com/python-advent-of-code/) talks about this simple
state machine.
"""

from dataclasses import dataclass
from typing import Dict, List

@dataclass
class StateMachine:
    memory: Dict[str, int]
    program: List[str]

    def run(self):
        """Run the program"""
        current_line = 0
        while current_line < len(self.program):
            instruction = self.program[current_line]

            # Set a register to a value
            if instruction.startswith("set "):
                register, value = instruction[4], int(instruction[6:])
                self.memory[register] = value

            # Increase the value in a register by 1
            elif instruction.startswith("inc "):
                register = instruction[4]
                self.memory[register] += 1

            # Move the line pointer
            current_line += 1
