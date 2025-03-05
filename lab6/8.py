import os

def check_path_and_get_details(path):
    if os.path.exists(path):
        dir_name = os.path.dirname(path)
        file_name = os.path.basename(path)
        print(f"Путь существует.")
        print(f"Имя каталога: {dir_name}")
        print(f"Имя файла: {file_name}")
    else:
        print("Путь не существует.")

path = "/путь/к/файлу/или/каталогу"
check_path_and_get_details(path)
