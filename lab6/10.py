def write_list_to_file(file_path, data_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(f"{item}\n")

data = ['яблоко', 'банан', 'вишня']
file_path = "/путь/к/файлу.txt"
write_list_to_file(file_path, data)
