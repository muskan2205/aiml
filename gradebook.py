grade_book = {}

def add_student():
    name = input("Enter student's name: ")
    grades = input("Enter grades separated by space: ")
    grade_list = list(map(float, grades.split()))
    grade_book[name] = grade_list
    print(f"{name} added with grades {grade_list}.\n")
def view_students():
    if not grade_book:
        print("No students in the grade book.\n")
    else:
        for student, grades in grade_book.items():
            print(f"{student}: Grades = {grades}")
        print()
def calculate_average():
    name = input("Enter student's name to calculate average: ")
    if name in grade_book:
        avg = sum(grade_book[name]) / len(grade_book[name])
        print(f"{name}'s average grade is {avg:.2f}\n")
    else:
        print("Student not found.\n")
def menu():
    while True:
        print("Grade Book Menu")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Calculate Average Grade")
        print("4. Exit")
        choice = input("Choose an option: ")
         
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            print("Exiting Grade Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
