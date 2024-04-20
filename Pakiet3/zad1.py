def double_list_elements(numbers):
    return [x * 2 for x in numbers]



original_list = [1, 2, 3, 4, 5]
doubled_list = double_list_elements(original_list)

print("Oryginalna lista:", original_list)  # Oryginalna lista: [1, 2, 3, 4, 5]
print("Lista po podwojeniu:", doubled_list)  # Lista po podwojeniu: [2, 4, 6, 8, 10]
