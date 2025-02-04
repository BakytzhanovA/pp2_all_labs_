def unique_elements(list):
    result = []
    for element in list:
        if element not in result:
            result.append(element)
    return result

list = [1, 2, 3, 1, 4, 3, 5, 4]
print(f"Уникальные элементы: {unique_elements(list)}")
