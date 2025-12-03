import re


def max_joltage_from_bank(bank: str, num_to_turn_on: int) -> int:
    starting_index: int = 0
    vals_to_keep: str = ""
    for i in range(1 - num_to_turn_on, 0):
        vals_to_keep += max(bank[(starting_index):i])
        bank = bank[starting_index:]
        starting_index = bank.find(vals_to_keep[-1]) + 1
    vals_to_keep += max(bank[(starting_index):])
    return int(vals_to_keep)


if __name__ == "__main__":
    with open("2025/input/joltages.txt") as f:
        banks_raw = f.readlines()
    banks: list[str] = [bank.strip() for bank in banks_raw]

    sum_of_max_joltages_2 = sum([max_joltage_from_bank(bank, 2) for bank in banks])
    sum_of_max_joltages_12 = sum([max_joltage_from_bank(bank, 12) for bank in banks])
    print(f"{sum_of_max_joltages_2=}, {sum_of_max_joltages_12=}")
