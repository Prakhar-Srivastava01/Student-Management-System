import csv
import os

FILE_NAME = "students.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Course"])

def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, course])

    print("Student added successfully!")

def view_students():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_student():
    search_id = input("Enter Student ID to search: ")
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["ID"] == search_id:
                print("Student Found:", row)
                found = True
                break

    if not found:
        print("Student not found.")

def delete_student():
    delete_id = input("Enter Student ID to delete: ")
    rows = []
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["ID"] != delete_id:
                rows.append(row)
            else:
                found = True

    if found:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Age", "Course"])
            writer.writeheader()
            writer.writerows(rows)
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")