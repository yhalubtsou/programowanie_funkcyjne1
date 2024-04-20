def calculate_tuple_stats(number_tuple):
    total = sum(number_tuple)
    average = total / len(number_tuple)
    return total, average

numbers = (10, 20, 30, 40, 50)
total_sum, average_value = calculate_tuple_stats(numbers)
print("Suma:", total_sum)
print("Średnia:", average_value)
