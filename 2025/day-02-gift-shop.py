import re


def identify_rulebreaking_ids_in_range(
    a: int, b: int, only_one_repeat_disallowed: bool
) -> list[int]:
    regex = r"^(\d+)\1$" if only_one_repeat_disallowed else r"^(\d+)\1+$"
    rulebreakers: list[int] = []
    for n in range(a, b + 1):
        if re.match(regex, str(n)):
            rulebreakers.append(n)
    return rulebreakers


if __name__ == "__main__":
    with open("2025/input/product_ids.txt") as f:
        ids_line = f.readlines()
    id_ranges: list[tuple[int, ...]] = [
        tuple(int(id_) for id_ in id_range.strip().split("-"))
        for id_range in ids_line[0].split(",")
    ]

    rulebreakers1: list[int] = [
        n
        for (a, b) in id_ranges
        for n in identify_rulebreaking_ids_in_range(a, b, True)
    ]
    rulebreakers2: list[int] = [
        n
        for (a, b) in id_ranges
        for n in identify_rulebreaking_ids_in_range(a, b, False)
    ]
    print(f"{sum(rulebreakers1)=}, {sum(rulebreakers2)=}")
