def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input("Введите количество граммов: "))
print(f"{grams} граммов = {grams_to_ounces(grams)} унций")
