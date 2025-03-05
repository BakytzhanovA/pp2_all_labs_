import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):  
            os.remove(path)
            print(f"Файл {path} был удален.")
        else:
            print(f"Нет прав на удаление файла {path}.")
    else:
        print(f"Файл {path} не существует.")

file_path = "/путь/к/файлу/для/удаления.txt"
delete_file(file_path)
