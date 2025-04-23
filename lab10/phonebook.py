import sqlite3
import csv

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

# --- Функция добавления контакта через консоль ---
def add_contact_console():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    try:
        cursor.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("[+] Контакт добавлен.")
    except sqlite3.IntegrityError:
        print("[!] Такой номер уже существует.")

# --- Функция загрузки контактов из CSV файла (ИСПРАВЛЕННАЯ) ---
def add_contact_from_csv():
    file_path = input("Введите путь к CSV файлу (формат: имя,телефон): ")
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            # Пропускаем заголовок, если он есть
            headers = next(csv_reader, None)
            
            success_count = 0
            skip_count = 0
            
            for row in csv_reader:
                if len(row) >= 2:  # Проверяем, что есть хотя бы 2 колонки
                    name = row[0].strip()
                    phone = row[1].strip()
                    
                    try:
                        cursor.execute(
                            "INSERT INTO PhoneBook (first_name, phone) VALUES (?, ?)",
                            (name, phone)
                        )
                        success_count += 1
                    except sqlite3.IntegrityError:
                        print(f"[!] Пропуск дубликата: {phone}")
                        skip_count += 1
                    except Exception as e:
                        print(f"[!] Ошибка при добавлении {name}, {phone}: {str(e)}")
                        skip_count += 1
            
            conn.commit()
            print(f"\n[+] Импорт завершен. Успешно: {success_count}, пропущено: {skip_count}")
            
    except FileNotFoundError:
        print("[!] Файл не найден. Проверьте путь.")
    except Exception as e:
        print(f"[!] Произошла ошибка: {str(e)}")

# --- Функция обновления контакта ---
def update_contact():
    phone = input("Введите номер телефона контакта для обновления: ")
    cursor.execute("SELECT * FROM PhoneBook WHERE phone = ?", (phone,))
    if not cursor.fetchone():
        print("[!] Контакт с таким номером не найден.")
        return
    
    print("Что вы хотите изменить?")
    print("1. Имя")
    print("2. Телефон")
    choice = input("Выберите опцию (1-2): ").strip()
    
    if choice == '1':
        new_name = input("Введите новое имя: ")
        cursor.execute("UPDATE PhoneBook SET first_name = ? WHERE phone = ?", (new_name, phone))
        conn.commit()
        print("[+] Имя обновлено.")
    elif choice == '2':
        new_phone = input("Введите новый телефон: ")
        try:
            cursor.execute("UPDATE PhoneBook SET phone = ? WHERE phone = ?", (new_phone, phone))
            conn.commit()
            print("[+] Телефон обновлен.")
        except sqlite3.IntegrityError:
            print("[!] Такой номер уже существует.")
    else:
        print("[!] Неверный выбор.")

# --- Функция поиска контактов с фильтрами ---
def search_contact():
    print("Критерии поиска:")
    print("1. По имени")
    print("2. По номеру телефона")
    print("3. По части имени")
    choice = input("Выберите опцию поиска (1-3): ").strip()
    
    if choice == '1':
        name = input("Введите точное имя: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE first_name = ?", (name,))
    elif choice == '2':
        phone = input("Введите точный номер: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE phone = ?", (phone,))
    elif choice == '3':
        name_part = input("Введите часть имени: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE first_name LIKE ?", ('%' + name_part + '%',))
    else:
        print("[!] Неверный выбор.")
        return
    
    results = cursor.fetchall()
    if results:
        print("\nРезультаты поиска:")
        for row in results:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("[!] Ничего не найдено.")

# --- Функция удаления контакта ---
def delete_contact():
    print("Удалить по:")
    print("1. Имени")
    print("2. Номеру телефона")
    choice = input("Выберите опцию (1-2): ").strip()
    
    if choice == '1':
        name = input("Введите имя для удаления: ")
        cursor.execute("DELETE FROM PhoneBook WHERE first_name = ?", (name,))
    elif choice == '2':
        phone = input("Введите номер для удаления: ")
        cursor.execute("DELETE FROM PhoneBook WHERE phone = ?", (phone,))
    else:
        print("[!] Неверный выбор.")
        return
    
    conn.commit()
    print("[+] Контакт(ы) удален(ы), если существовал(и).")

# --- Функция показа всех контактов ---
def show_all_contacts():
    cursor.execute("SELECT * FROM PhoneBook ORDER BY first_name")
    rows = cursor.fetchall()
    if rows:
        print("\nВсе контакты:")
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("[!] Телефонная книга пуста.")

# --- Главное меню ---
def main_menu():
    while True:
        print("\n--- ТЕЛЕФОННАЯ КНИГА ---")
        print("1. Добавить контакт (консоль)")
        print("2. Добавить контакты из CSV файла")
        print("3. Обновить контакт")
        print("4. Поиск контактов")
        print("5. Удалить контакт")
        print("6. Показать все контакты")
        print("7. Выход")

        choice = input("Выберите действие (1-7): ").strip()

        if choice == '1':
            add_contact_console()
        elif choice == '2':
            add_contact_from_csv()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            show_all_contacts()
        elif choice == '7':
            print("Выход...")
            break
        else:
            print("[!] Неверный выбор.")

    conn.close()

# --- Запуск программы ---
if __name__ == "__main__":
    main_menu()