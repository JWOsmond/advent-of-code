import re

import numpy as np


def solve_problem(numbers: list[str], operation: str) -> int:
    if operation == "+":
        result: int = 0
        for number in numbers:
            result += int(number)
    else:
        result: int = 1
        for number in numbers:
            result *= int(number)
    return result


if __name__ == "__main__":
    with open("2025/input/homework.txt") as f:
        lines: list[str] = [line.strip() for line in f.readlines()]
    
    homework: list[list[str]] = np.array(
        [re.sub(r"\s+", " ", line).split(" ") for line in lines]
    ).T
    total: int = 0
    for problem in homework:
        *numbers, operation = problem
        total += solve_problem(numbers, operation=operation)
    print(f"{total=}")