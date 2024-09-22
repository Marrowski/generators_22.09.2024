def simple_generator(n):
    for i in range(2, n):
        if i % 2 != 0:
            yield i


gen = simple_generator(20)

for j in gen:
    print(j)