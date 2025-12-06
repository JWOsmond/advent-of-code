import re

import numpy as np


def process_problem_1(lines: list[str]) -> np.ndarray:
    return np.array([re.sub(r"\s+", " ", line.strip()).split(" ") for line in lines]).T


def process_problem_2(lines: list[str]):
    start_indices: list[int] = []
    operations: list[str] = []
    for idx, char in enumerate(lines[-1]):
        if char != " ":
            start_indices.append(idx)
            operations.append(char)
    start_indices.append(len(lines[-1]) + 2)
    new_lines: list[list[str]] = [[] for _ in enumerate(lines[:-1])]
    for i, start_idx in enumerate(start_indices[:-1]):
        for j, line in enumerate(lines[:-1]):
            new_lines[j].append(line[start_idx : (start_indices[i + 1] - 1)])
    new_lines.append(operations)
    return np.array(new_lines).T


def solve_problem_1(numbers: list[str], operation: str) -> int:
    if operation == "+":
        result: int = 0
        for number in numbers:
            result += int(number)
    else:
        result: int = 1
        for number in numbers:
            result *= int(number)
    return result


def solve_problem_2(numbers: list[str], operation: str) -> int:
    numbers = [number.replace(" ", "x") for number in numbers]

    new_numbers: list[int] = []
    for pos, _ in enumerate(numbers[0]):
        new_numbers.append(
            int("".join([number[pos] for number in numbers]).replace("x", ""))
        )

    if operation == "+":
        result: int = 0
        for number in new_numbers:
            result += int(number)
    else:
        result: int = 1
        for number in new_numbers:
            result *= int(number)
    return result


if __name__ == "__main__":
    with open("2025/input/homework.txt") as f:
        lines: list[str] = f.readlines()

    homework_1: np.ndarray = process_problem_1(lines)
    total_1: int = 0
    for problem in homework_1:
        *numbers, operation = problem
        total_1 += solve_problem_1(numbers, operation=operation)
    homework_2: np.ndarray = process_problem_2(lines)
    total_2: int = 0
    for problem in homework_2:
        *numbers, operation = problem.tolist()
        total_2 += solve_problem_2(numbers, operation=operation)
    print(f"{total_1=}, {total_2}")
