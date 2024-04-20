def square(x):
    return x ** 2

def add_five(x):
    return x + 5

def combine_functions(*args):
    def combined_function(x):
        result = x
        for func in args:
            result = func(result)
        return result
    return combined_function

numbers = [1, 2, 3, 4, 5]

combined_function = combine_functions(square, add_five)

result = list(map(combined_function, numbers))

print("Wyniki zastosowania połączonej funkcji do listy liczb:", result)
