def copy_file_contents(src_path, dst_path):
    with open(src_path, 'r', encoding='utf-8') as src_file:
        content = src_file.read()
    
    with open(dst_path, 'w', encoding='utf-8') as dst_file:
        dst_file.write(content)

src_path = "/путь/к/исходному/файлу.txt"
dst_path = "/путь/к/новому/файлу.txt"
copy_file_contents(src_path, dst_path)
