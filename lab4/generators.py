def squares(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input("Введите число N: "))
for square in squares(n):
    print(square)
    
#2
def even_numbers_D(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Введите число N: "))
even_numbers = [str(num) for num in even_numbers_D(n)]
print(", ".join(even_numbers))

#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Введите число N: "))
for num in divisible_by_3_and_4(n):
    print(num)
    
#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
for square in squares(a, b):
    print(square)


#5
def all_nums(n):
    while n>=0:
        yield n
        n=-1

n = int(input("Введите число: "))
print(all_nums(n))

