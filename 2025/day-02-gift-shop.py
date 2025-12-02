import re


def identify_rulebreaking_id1(n: int) -> bool:
    return bool(re.match(r"^(\d+)\1$", str(n)))


def identify_rulebreaking_ids_in_range1(a: int, b: int) -> list[int]:
    rulebreakers: list[int] = []
    for n in range(a, b + 1):
        if identify_rulebreaking_id1(n):
            rulebreakers.append(n)
    return rulebreakers


def identify_rulebreaking_id2(n: int) -> bool:
    return bool(re.match(r"^(\d+)\1+$", str(n)))


def identify_rulebreaking_ids_in_range2(a: int, b: int) -> list[int]:
    rulebreakers: list[int] = []
    for n in range(a, b + 1):
        if identify_rulebreaking_id2(n):
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
        n for (a, b) in id_ranges for n in identify_rulebreaking_ids_in_range1(a, b)
    ]
    rulebreakers2: list[int] = [
        n for (a, b) in id_ranges for n in identify_rulebreaking_ids_in_range2(a, b)
    ]
    print(f"{sum(rulebreakers1)=}, {sum(rulebreakers2)=}")
