def map_nested(nested_list, func):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.append(map_nested(item, func))
        else:
            result.append(func(item))
    return result

nested_list = [1, [2, 3], [4, [5, 6]], 7]
mapped_list = map_nested(nested_list, lambda x: x * 2)

print("Zagnieżdżona lista:", nested_list)  # Zagnieżdżona lista: [1, [2, 3], [4, [5, 6]], 7]
print("Po zastosowaniu funkcji:", mapped_list)  # Po zastosowaniu funkcji: [2, [4, 6], [8, [10, 12]], 14]
