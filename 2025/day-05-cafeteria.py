import pandas as pd


def construct_distinct_ranges(ranges_ints: list[list[int]]):
    mins: list[int] = [range_[0] for range_ in ranges_ints]
    maxs: list[int] = [range_[1] for range_ in ranges_ints]
    df = (
        pd.DataFrame({"min": mins, "max": maxs})
        .sort_values("min")
        .drop_duplicates()
        .reset_index(drop=True)
    )

    # if the maxima are not in order after having ordered by minima, then an
    # out-of-order maximum indicates a range being a subset of the previous range.
    # These subset ranges can be removed.
    indices_to_keep: list[bool] = [True]
    for idx, (min_, max_) in df[1:].iterrows():
        if max_ <= df.loc[: (idx - 1), "max"].max():  # pyright: ignore[reportOperatorIssue]
            indices_to_keep.append(False)
        else:
            indices_to_keep.append(True)
    df = df.loc[indices_to_keep].reset_index(drop=True)

    # Now, if the start of a range is less than the previous maximum, we know that the
    # ranges overlap. Reset the start of the range to be one more than the previous
    # maximum.
    for idx, (min_, max_) in df.loc[1:].iterrows():
        if min_ <= df.loc[idx - 1, "max"]:  # pyright: ignore[reportOperatorIssue]
            df.loc[idx, "min"] = df.loc[idx - 1, "max"] + 1  # pyright: ignore[reportArgumentType, reportCallIssue, reportOperatorIssue]
    df["range_size"] = df["max"] - df["min"] + 1
    df = df.loc[df["range_size"] > 0]
    return df


if __name__ == "__main__":
    with open("2025/input/ingredients.txt") as f:
        ingredients: list[str] = [ingredient.strip() for ingredient in f.readlines()]

    ranges: list[str] = [ingredient for ingredient in ingredients if "-" in ingredient]
    to_check: list[int] = [
        int(ingredient)
        for ingredient in ingredients
        if ingredient != "" and "-" not in ingredient
    ]
    ranges_ints: list[list[int]] = [
        [int(int_) for int_ in range_.split("-")] for range_ in ranges
    ]
    fresh_ingredients: list[int] = []
    for id_ in to_check:
        for range_ in ranges_ints:
            if id_ >= range_[0] and id_ <= range_[1]:
                fresh_ingredients.append(id_)
                break

    distinct_ranges: pd.DataFrame = construct_distinct_ranges(ranges_ints)
    print(f"{len(fresh_ingredients)=}, {sum(distinct_ranges["range_size"])=}")
