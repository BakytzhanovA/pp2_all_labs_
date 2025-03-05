import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    
    print(f"Путь существует: {exists}")
    print(f"Чтение разрешено: {readable}")
    print(f"Запись разрешена: {writable}")
    print(f"Исполнение разрешено: {executable}")

path = "/путь/к/каталогу/или/файлу"
check_access(path)
