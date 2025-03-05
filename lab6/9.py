def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)

file_path = "/путь/к/файлу.txt"
lines_count = count_lines_in_file(file_path)
print(f"Количество строк в файле: {lines_count}")
