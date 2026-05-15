students = {}

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        students[name] = marks

        print("Student Added Successfully")

    elif choice == 2:

        print("\nStudent Records")

        for name, marks in students.items():
            print(name, "=", marks)

    elif choice == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
