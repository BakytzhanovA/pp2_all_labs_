def count_case_letters(input_string):
    upper_case = sum(1 for char in input_string if char.isupper())
    lower_case = sum(1 for char in input_string if char.islower())
    return upper_case, lower_case

string = "Hello World"

upper, lower = count_case_letters(string)

print(f"Количество заглавных букв: {upper}")
print(f"Количество строчных букв: {lower}")
