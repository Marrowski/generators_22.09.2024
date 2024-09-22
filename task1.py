def generator_a(new_list: list):
    yield new_list[::-1]


new_gen = generator_a([1, 2, 3, 4, 5, 6, 7, 8])

for i in new_gen:
    print(i)

