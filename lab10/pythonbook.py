import sqlite3

# --- Подключение и создание таблицы ---
conn = sqlite3.connect("phonebook.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        phone TEXT NOT NULL UNIQUE
    )
''')
conn.commit()

# --- Добавление контакта ---
def add_contact():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    try:
        cursor.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("[+] Контакт добавлен.")
    except sqlite3.IntegrityError:
        print("[!] Такой номер уже существует.")

# --- Поиск контакта ---
def search_contact():
    name = input("Введите имя для поиска: ")
    cursor.execute("SELECT * FROM PhoneBook WHERE first_name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("[!] Ничего не найдено.")

# --- Удаление контакта ---
def delete_contact():
    name = input("Введите имя для удаления: ")
    cursor.execute("DELETE FROM PhoneBook WHERE first_name = ?", (name,))
    conn.commit()
    print("[+] Если контакт существовал — он удалён.")

# --- Показ всех контактов ---
def show_all_contacts():
    cursor.execute("SELECT * FROM PhoneBook")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("[!] Телефонная книга пуста.")

# --- Главное меню ---
def main_menu():
    while True:
        print("\n--- Телефонная книга ---")
        print("1. Добавить контакт")
        print("2. Поиск контактов")
        print("3. Удалить контакт")
        print("4. Показать все контакты")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            show_all_contacts()
        elif choice == '5':
            print("Выход...")
            break
        else:
            print("[!] Неверный выбор.")

    conn.close()

# --- Запуск программы ---
if __name__ == "__main__":
    main_menu()
