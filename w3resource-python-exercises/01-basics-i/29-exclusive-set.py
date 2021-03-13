def exclusive_in_set(set_1, set_2):
    set_result = set()
    for item in set_1:
        if not item in set_2:
            set_result.add(item)
    print(set_result)

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

exclusive_in_set(color_list_1, color_list_2)
