def reverse_words():
    sentence = input("Введите предложение: ")
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    print(f"Перевернутое предложение: {reversed_sentence}")

reverse_words()
