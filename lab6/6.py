import os

def list_files_and_dirs(path):
    files = []  
    dirs = []   

    for item in os.listdir(path):  
        full_path = os.path.join(path, item)  

        if os.path.isdir(full_path):
            dirs.append(item)  
        elif os.path.isfile(full_path):
            files.append(item)  
    
    print("Каталоги:", dirs)
    print("Файлы:", files)
    print("Все элементы:", os.listdir(path))  

# Жол
path = "C:/Users/User/Documents"  
list_files_and_dirs(path)
