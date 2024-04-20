def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))



def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

file_path = 'large_file.txt'
lines_gen = read_large_file(file_path)
for line in lines_gen:
    print(line)
