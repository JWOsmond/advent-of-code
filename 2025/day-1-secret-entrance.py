class Dial1:
    def __init__(self, start_no: int = 50):
        self.num: int = start_no
        self.zero_count: int = 0

    def turn(self, instruction: str):
        turn_size_str = instruction[1:]
        if len(turn_size_str) >= 3:
            turn_size: int = int(turn_size_str[-2:])
        else:
            turn_size: int = int(turn_size_str)

        if (dir := instruction[0].upper()) == "R":
            anti_clockwise_turn = turn_size
            clockwise_turn = 100 - turn_size
        else:
            clockwise_turn = turn_size
            anti_clockwise_turn = 100 - turn_size

        if self.num + anti_clockwise_turn > 99:
            self.num -= clockwise_turn
        else:
            self.num += anti_clockwise_turn

        if self.num == 0:
            self.zero_count += 1


class Dial2:
    def __init__(self, start_no: int = 50):
        self.num: int = start_no
        self.zero_count: int = 0

    def turn(self, instruction: str):
        turn_size_str = instruction[1:]
        if len(turn_size_str) >= 3:
            turn_size: int = int(turn_size_str[-2:])
            self.zero_count += int(turn_size_str[:-2])
        else:
            turn_size: int = int(turn_size_str)

        if (dir := instruction[0].upper()) == "R":
            anti_clockwise_turn = turn_size
            clockwise_turn = 100 - turn_size
        else:
            clockwise_turn = turn_size
            anti_clockwise_turn = 100 - turn_size

        if dir == "R" and self.num + anti_clockwise_turn > 99:
            if self.num != 0:
                self.zero_count += 1
            self.num -= clockwise_turn
        elif dir == "R":
            self.num += anti_clockwise_turn
            if self.num == 0 and anti_clockwise_turn != 0:
                self.zero_count += 1
        elif dir == "L" and self.num - clockwise_turn < 0:
            if self.num != 0:
                self.zero_count += 1
            self.num += anti_clockwise_turn
        else:
            self.num -= clockwise_turn
            if self.num == 0 and clockwise_turn != 0:
                self.zero_count += 1


if __name__ == "__main__":
    with open("2025/input/directions.txt") as f:
        directions_lines = f.readlines()
    directions = [direction.strip() for direction in directions_lines]

    dial1 = Dial1()
    dial2 = Dial2()
    for direction in directions:
        dial1.turn(direction)
        dial2.turn(direction)

    print(f"{dial1.zero_count=}; {dial2.zero_count=}")
