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


def count_acceptable_rolls(data: np.ndarray) -> tuple[int, list[tuple[int, int]]]:
    count: int = 0
    nrows, ncols = data.shape
    indices: list[tuple[int, int]] = []
    for i in range(0, nrows):
        for j in range(0, ncols):
            if data[i, j] == "@" and count_adjacent_rolls(data, i, j) < 4:
                count += 1
                indices.append((i, j))
    return count, indices


def count_and_remove_acceptable_rolls_iteratively(
    data: np.ndarray,
) -> tuple[int, np.ndarray]:
    count: int = 0
    count_diff: int = -1
    while count_diff != 0:
        count_diff, updated_indices = count_acceptable_rolls(data)
        count += count_diff
        for i, j in updated_indices:
            data[i, j] = "."
    return count, data


if __name__ == "__main__":
    with open("2025/input/paper_rolls.txt") as f:
        rolls_raw = f.readlines()

    rolls: np.ndarray = np.array([list(roll.strip()) for roll in rolls_raw])

    removal_1 = count_acceptable_rolls(rolls)
    removal_2 = count_and_remove_acceptable_rolls_iteratively(rolls)
    part_1_answer: int = removal_1[0]
    part_2_answer: int = removal_2[0]
    print(f"{part_1_answer=}, {part_2_answer=}")
