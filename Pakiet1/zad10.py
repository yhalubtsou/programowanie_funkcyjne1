def even_numbers_generator():
    n = 0
    while True:
        yield n
        n += 2

gen = even_numbers_generator()
first_5_evens = [next(gen) for _ in range(5)]
print(first_5_evens)
