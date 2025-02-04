import itertools

def string_permutations():
    s = input("Введите строку: ")
    permutations = [''.join(p) for p in itertools.permutations(s)]
    for p in permutations:
        print(p)

string_permutations()
