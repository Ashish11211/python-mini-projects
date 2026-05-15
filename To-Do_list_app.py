tasks = []

while True:

    print("\n1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        task = input("Enter task: ")
        tasks.append(task)

    elif choice == 2:

        print("\nTasks")

        for t in tasks:
            print("-", t)

    elif choice == 3:

        task = input("Enter task to delete: ")

        if task in tasks:
            tasks.remove(task)

    elif choice == 4:
        break
