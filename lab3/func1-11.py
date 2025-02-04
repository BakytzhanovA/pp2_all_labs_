def is_palindrome(word):
    word = word.lower().replace(" ", "") 
    return word == word[::-1] 

word = input("Введите слово или фразу: ")
if is_palindrome(word):
    print("Это палиндром!")
else:
    print("Это не палиндром.")