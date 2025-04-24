import psycopg2
import csv

import configparser

config = configparser.ConfigParser()
config.read("database.ini")

params = config["postgresql"]
conn = psycopg2.connect(**params)

cur = conn.cursor()

def insert_manual():
    first = input("First name: ")
    last = input("Last name: ")
    phone = input("Phone number: ")
    cur.execute("CALL upsert_user(%s, %s, %s)", (first, last, phone))
    conn.commit()
    print("✅ User inserted or updated")

def insert_from_csv(file_path):
    names = []
    lasts = []
    phones = []
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            names.append(row[0])
            lasts.append(row[1])
            phones.append(row[2])
    cur.execute("CALL bulk_insert_users(%s, %s, %s, NULL)", (names, lasts, phones))
    conn.commit()
    print("📁 Bulk insert attempted (check DB for invalid numbers)")

def update_user():
    phone = input("Enter phone number to update: ")
    new_name = input("New first name: ")
    new_last = input("New last name: ")
    cur.execute("CALL upsert_user(%s, %s, %s)", (new_name, new_last, phone))
    conn.commit()
    print("✅ Updated")

def search_user():
    pattern = input("Enter pattern to search (name/surname/phone): ")
    cur.execute("SELECT * FROM search_phonebook(%s::TEXT)", (pattern,))
    results = cur.fetchall()
    if not results:
        print("No matching records.")
    else:
        print("Found:")
        for row in results:
            print(row)

def delete_user():
    first = input("Enter first name (or leave empty): ").strip()
    last = input("Enter last name (or leave empty): ").strip()
    phone = input("Enter phone to delete (or leave empty): ").strip()

    if phone:
        cur.execute("CALL delete_user_by_phone(%s)", (phone,))
    elif first and last:
        cur.execute("CALL delete_user_by_name_and_surname(%s, %s)", (first, last))
    else:
        print("provide normally")

    conn.commit()

def paginate():
    limit = int(input("Enter number of rows per page: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def addlist():
    while True:
        first = input("First name: ")
        last = input("Last name: ")
        phone = input("Phone number: ")
        cur.execute("CALL upsert_user(%s, %s, %s)", (first, last, phone))
        conn.commit()
        print("✅ User inserted or updated")
        to_stop = input("Write stop to stop or leave it empty to continue: ")
        if to_stop == "stop":
            break

def main():
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Add user manually")
        print("2. Upload users from CSV")
        print("3. Update user")
        print("4. Search user")
        print("5. Delete user")
        print("6. Show paginated list")
        print("7. ADD many users in a row")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_manual()
        elif choice == "2":
            insert_from_csv("phonebook.csv")
        elif choice == "3":
            update_user()
        elif choice == "4":
            search_user()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            paginate()
        elif choice == "7":
            addlist()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

    cur.close()
    conn.close()

main()