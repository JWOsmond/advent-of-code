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
    print(f"{len(fresh_ingredients)=}")
