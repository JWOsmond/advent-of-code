import re

import numpy as np


class Beam:
    def __init__(self, manifold: np.ndarray):
        self.manifold = manifold
        self.start_point = manifold[0, :].tolist().index("S")
        self.tachyon_points: list[int] = [self.start_point]
        self.splits: int = 0

    def hit_splitter(self, row: int, index: int) -> None:
        self.splits += 1
        self.tachyon_points.remove(index)
        if index > 0:
            self.manifold[row, index - 1] = str(
                int(self.manifold[row - 1, index]) + int(self.manifold[row, index - 1])
            )
            if (index - 1) not in self.tachyon_points:
                self.tachyon_points.append(index - 1)
        if index < (self.manifold.shape[1] - 1):
            self.manifold[row, index + 1] = str(
                int(self.manifold[row - 1, index]) + int(self.manifold[row, index + 1])
            )
            if (index + 1) not in self.tachyon_points:
                self.tachyon_points.append(index + 1)

    def traverse(self) -> None:
        print("---------------")
        for row in range(1, self.manifold.shape[0]):
            old_points: list[int] = sorted(self.tachyon_points.copy())
            for point in old_points:
                # only do if point-1 >=0 etc., and ensure no duplicates
                if self.manifold[row, point] == "^":
                    self.hit_splitter(row, point)
                else:
                    self.manifold[row, point] = (
                        str(
                            int(self.manifold[row, point])
                            + int(self.manifold[row - 1, point])
                        )
                        if self.manifold[row - 1, point] != "S"
                        else "1"
                    )
        self.number_possible_paths = sum([int(val) for val in self.manifold[-1, :]])


if __name__ == "__main__":
    with open("2025/input/manifold.txt") as f:
        manifold_lines: list[str] = f.readlines()

    manifold = np.array(
        [list(re.sub(r"\.", "0", line.strip())) for line in manifold_lines],
        dtype=np.dtype("U100"),  # required so strings can be longer than 1 character
    )
    print(manifold)
    beam = Beam(manifold)
    beam.traverse()
    print(f"{beam.splits=}, {beam.number_possible_paths=}")
