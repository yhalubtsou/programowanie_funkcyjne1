filter_even = lambda numbers: list(filter(lambda x: x % 2 == 0, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even(numbers)
print("Liczby parzyste:", even_numbers)


rectangle_area = lambda length, width: length * width

length = 5
width = 10
area = rectangle_area(length, width)
print("Pole prostokąta o bokach", length, "i", width, "wynosi:", area)

