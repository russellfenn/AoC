"""
Day 02 - Red-Nosed Reports

Part 1 puzzle input is a list of Reports, where each report is a 
series of Levels (integers).

Levels are "safe" if they
- either ALL increase or ALL decrease

  - find the difference between successive levels -> either all positive or negative

- successive levels differ by 1, 2, or 3

  - Any 0 makes it unsafe
  - Any >= 4 is unsafe
"""
type Report = list[int]
type Deltas = list[int]  # length will be one less than Report


def parse_puzzle_input(puzzle_str: list[str]) -> list[Report]:
    """Read the puzzle input as a list of strings"""
    puzzle: list[Report] = []
    for line in puzzle_str:
        report: Report = [int(l) for l in line.split()]
        puzzle.append(report)
    return puzzle


def calc_deltas(report: Report) -> Deltas:
    """Find the delta from each element in the list"""
    return [e[1] - report[e[0]] for e in enumerate(report[1:])]


def is_part_1_safe(report: Report) -> bool:
    """Are the Levels in this Report safe according to Part 1 rules?
    """
    deltas: Deltas = calc_deltas(report)
    safe_values: list[int] = [-3, -2, -1, 1, 2, 3]
    # Ensure every value in the safe range
    if not all([d in safe_values for d in deltas]):
        return False
    # Ensure all increasing
    if deltas[0] > 0:
        if not all([d > 0 for d in deltas]):
            return False
    else:
        if not all([d < 0 for d in deltas]):
            return False
    return True


def solve_part_1(reports: list[Report]) -> int:
    """Count how many reports are 'safe'"""
    safety_report: list[bool] = [is_part_1_safe(r) for r in reports]
    return sum(safety_report)  # when summed, True counts as 1


def problem_dampener(report: Report) -> Report | None:
    """Tries to remove 'problem' listings from a single Report.
       If the report cannot be made safe, returns None.

       Try to make reports safe by removing one element at a time.
    """
    # if already safe, do nothing
    if is_part_1_safe(report):
        return report
    for i in range(len(report)):
        test_report: Report = report.copy()
        del test_report[i]
        if is_part_1_safe(test_report):
            return test_report
    return None


def solve_part_2(reports: list[Report]) -> int:
    """Count how many reports are 'safe' after running
       them through the Problem Dampener
    """
    safety_report: list[bool] = []
    for r in reports:
        if problem_dampener(r):
            safety_report.append(True)  # we could remove a value to make it safe
        else:
            safety_report.append(False)
    return sum(safety_report)  # when summed, True counts as 1


if __name__ == "__main__":
    with open("d02.input", "r", encoding="UTF-8") as f:
        reports_in: list[Report] = parse_puzzle_input(f.read().splitlines())
    print(f"[Part 1] There are {solve_part_1(reports_in)} safe reports.")
    print(f"[Part 2] Using the Problem Dampener, there are now {solve_part_2(reports_in)} safe reports.")
