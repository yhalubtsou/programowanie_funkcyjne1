from functools import reduce

numbers = [10, 5, 8, 20, 15]

max_number = reduce(lambda x, y: x if x > y else y, numbers)
print("Największa liczba w liście:", max_number)

def calculate_average(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers)

average = calculate_average(numbers)
print("Średnia z listy liczb:", average)

