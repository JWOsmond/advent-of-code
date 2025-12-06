import re

import numpy as np


def process_problem_1(lines: list[str]) -> list[list[str]]:
    return np.array(
        [re.sub(r"\s+", " ", line.strip()).split(" ") for line in lines]
    ).T


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
        lines: list[str] = f.readlines()
    
    homework_1: list[list[str]] = process_problem_1(lines)
    total: int = 0
    for problem in homework_1:
        *numbers, operation = problem
        total += solve_problem(numbers, operation=operation)
    print(f"{total=}")