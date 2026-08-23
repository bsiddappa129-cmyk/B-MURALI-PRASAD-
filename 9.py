B MURALI PRASAD
KUB25EEE610
DATE : 23/08/2026

# ==========================================
# Student Record Management System
# Features: Add, View, Search, Update, Delete
# ==========================================

def display_menu():
    print("\n" + "="*40)
    print(" STUDENT RECORD MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add a New Student")
    print("2. View All Students")
    print("3. Search for a Student")
    print("4. Update Student Marks")
    print("5. Delete a Student")
    print("6. Exit System")
    print("="*40)

def add_student(students_list):
    print("\n--- Add New Student ---")
    roll_no = input("Enter Roll Number: ").strip()
    for student in students_list:
        if student["roll_no"] == roll_no:
            print("Error: Student already exists!")
            return
    name = input("Enter Name: ").strip()
    marks = input("Enter Marks: ").strip()
    student_dict = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }
    students_list.append(student_dict)
    print("Success: Student added!")

def view_students(students_list):
    if not students_list:
        print("\nNo records found.")
        return
    print("\n--- All Students ---")
    for student in students_list:
        print(f"Roll: {student['roll_no']} | Name: {student['name']} | Marks: {student['marks']}")

def search_student(students_list):
    print("\n--- Search Student ---")
    roll_no = input("Enter Roll Number: ").strip()
    for student in students_list:
        if student["roll_no"] == roll_no:
            print(f"Found: {student['name']} with {student['marks']} marks.")
            return
    print("Student not found.")

def update_student(students_list):
    print("\n--- Update Marks ---")
    roll_no = input("Enter Roll Number: ").strip()
    for student in students_list:
        if student["roll_no"] == roll_no:
            student["marks"] = input("Enter new marks: ").strip()
            print("Marks updated!")
            return
    print("Student not found.")

def delete_student(students_list):
    print("\n--- Delete Student ---")
    roll_no = input("Enter Roll Number: ").strip()
    for student in students_list:
        if student["roll_no"] == roll_no:
            students_list.remove(student)
            print("Record deleted!")
            return
    print("Student not found.")

def main():
    students = []
    while True:
        display_menu()
        choice = input("Enter choice (1-6): ").strip()
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

# End of Program
# Designed for managing records effectively.
