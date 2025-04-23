import sqlite3
from typing import List, Tuple

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

def search_by_pattern(pattern: str) -> List[Tuple]:
    cursor.execute('''
        SELECT * FROM PhoneBook 
        WHERE first_name LIKE ? OR phone LIKE ?
    ''', (f'%{pattern}%', f'%{pattern}%'))
    return cursor.fetchall()

def upsert_contact(name: str, phone: str) -> None:
    try:
        cursor.execute('''
            UPDATE PhoneBook SET phone = ? WHERE first_name = ?
        ''', (phone, name))
        
        if cursor.rowcount == 0:
            cursor.execute('''
                INSERT INTO PhoneBook (first_name, phone) VALUES (?, ?)
            ''', (name, phone))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"[!] Error: {e}")
        conn.rollback()

def batch_insert_users(users: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    invalid_entries = []
    
    for name, phone in users:
        if not phone.isdigit() or len(phone) < 5:
            invalid_entries.append((name, phone))
            continue
        
        try:
            upsert_contact(name, phone)
        except sqlite3.Error:
            invalid_entries.append((name, phone))
    
    return invalid_entries

def get_contacts_paginated(limit: int, offset: int) -> List[Tuple]:
    cursor.execute('''
        SELECT * FROM PhoneBook 
        LIMIT ? OFFSET ?
    ''', (limit, offset))
    return cursor.fetchall()

def delete_by_name_or_phone(identifier: str) -> None:
    try:
        cursor.execute('''
            DELETE FROM PhoneBook 
            WHERE first_name = ? OR phone = ?
        ''', (identifier, identifier))
        conn.commit()
    except sqlite3.Error as e:
        print(f"[!] Error: {e}")
        conn.rollback()

def add_contact():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    upsert_contact(name, phone)
    print("[+] Контакт добавлен/обновлён.")

def search_contact():
    pattern = input("Введите часть имени или номера для поиска: ")
    results = search_by_pattern(pattern)
    if results:
        for row in results:
            print(row)
    else:
        print("[!] Ничего не найдено.")

def delete_contact():
    identifier = input("Введите имя или номер для удаления: ")
    delete_by_name_or_phone(identifier)
    print("[+] Если контакт существовал — он удалён.")

def show_all_contacts():
    page_size = 5
    offset = 0
    
    while True:
        contacts = get_contacts_paginated(page_size, offset)
        
        if not contacts:
            if offset == 0:
                print("[!] Телефонная книга пуста.")
            else:
                print("[!] Больше контактов нет.")
            break
            
        for contact in contacts:
            print(contact)
            
        choice = input("Показать ещё? (y/n): ").lower()
        if choice != 'y':
            break
            
        offset += page_size

def batch_add_contacts():
    print("Введите контакты в формате 'Имя Телефон' (пустая строка для завершения):")
    users = []
    
    while True:
        entry = input().strip()
        if not entry:
            break
        parts = entry.split()
        if len(parts) >= 2:
            name = ' '.join(parts[:-1])
            phone = parts[-1]
            users.append((name, phone))
    
    if users:
        invalid = batch_insert_users(users)
        print(f"[+] Добавлено {len(users) - len(invalid)} контактов.")
        if invalid:
            print("[!] Некорректные данные:")
            for entry in invalid:
                print(entry)

def main_menu():
    while True:
        print("\n--- Телефонная книга ---")
        print("1. Добавить/обновить контакт")
        print("2. Поиск контактов")
        print("3. Удалить контакт")
        print("4. Показать все контакты (с пагинацией)")
        print("5. Массовое добавление контактов")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            show_all_contacts()
        elif choice == '5':
            batch_add_contacts()
        elif choice == '6':
            print("Выход...")
            break
        else:
            print("[!] Неверный выбор.")

    conn.close()

if __name__ == "__main__":
    main_menu()