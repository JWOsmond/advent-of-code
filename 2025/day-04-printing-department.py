import numpy as np


def count_adjacent_rolls(data: np.ndarray, a: int, b: int) -> int:
    count: int = 0
    nrows, ncols = data.shape
    for i in range(max(0, a - 1), min(nrows - 1, a + 1) + 1):
        for j in range(max(0, b - 1), min(ncols - 1, b + 1) + 1):
            if not (i == a and j == b):
                if data[i, j] == "@":
                    count += 1
    return count


def count_acceptable_rolls(data: np.ndarray) -> int:
    count: int = 0
    nrows, ncols = data.shape
    for i in range(0, nrows):
        for j in range(0, ncols):
            if data[i, j] == "@" and count_adjacent_rolls(data, i, j) < 4:
                count += 1
    return count


if __name__ == "__main__":
    with open("2025/input/paper_rolls.txt") as f:
        rolls_raw = f.readlines()

    rolls: np.ndarray = np.array([list(roll.strip()) for roll in rolls_raw])
    print(f"{count_acceptable_rolls(rolls)=}")
