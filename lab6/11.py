import string

def create_files():
    for letter in string.ascii_uppercase:  # Получаем буквы от A до Z
        file_name = f"{letter}.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"Этот файл называется {file_name}")

create_files()
