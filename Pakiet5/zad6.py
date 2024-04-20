words = ["apple", "banana", "avocado", "orange", "kiwi", "apricot"]

words_starting_with_a = list(filter(lambda word: word.startswith('a'), words))
print("Słowa zaczynające się na 'a':", words_starting_with_a)

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Kwadraty liczb:", squared_numbers)

