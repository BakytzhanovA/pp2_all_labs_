def all_true_in_tuple(input_tuple):
    return all(input_tuple)

my_tuple = (True, 1, "Hello", 5)

if all_true_in_tuple(my_tuple):
    print("Все элементы кортежа истинны.")
else:
    print("Не все элементы кортежа истинны.")
