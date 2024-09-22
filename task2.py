#За допомогою генератору
def pair_generator(num: list):
    for i in num:
        if i % 2 == 0:
            yield i ** 2


gen = pair_generator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

for j in gen:
    print(j)

#За допомогою циклу

def new_generator(num: list):
    yield num


gener = new_generator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in gener:
    for num in i:
        if num % 2 == 0:
            print(num ** 2)