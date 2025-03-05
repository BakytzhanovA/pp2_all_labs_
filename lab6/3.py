def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]

string = "A man a plan a canal Panama"

if is_palindrome(string):
    print(f"Строка '{string}' является палиндромом.")
else:
    print(f"Строка '{string}' не является палиндромом.")
