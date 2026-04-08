tasks = []
def show_tasks():
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks yet!")
while True:
    print("\n1. Add task\n2. Delete task\n3. Show tasks\n4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        show_tasks()
        del_task = int(input("Enter task number to delete: "))
        if 0 < del_task <= len(tasks):
            removed = tasks.pop(del_task-1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number")
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid input")