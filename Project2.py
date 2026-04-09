students = []

while True:
    print("\n1. Add Student\n2. Show Students\n3. Search\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "marks": marks})
        print("Student added!")

    elif choice == "2":
        for s in students:
            print(s)

    elif choice == "3":
        search = input("Enter name to search: ")
        found = False
        for s in students:
            if s["name"].lower() == search.lower():
                print("Found:", s)
                found = True
        if not found:
            print("Not found!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")