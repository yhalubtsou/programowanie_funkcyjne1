def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def calculate(operation, x, y):
    result = operation(x, y)
    return result

add_result = calculate(add, 5, 3)
subtract_result = calculate(subtract, 10, 4)

print("Wynik dodawania:", add_result)  # 8
print("Wynik odejmowania:", subtract_result)  # 6

