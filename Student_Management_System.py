students = {}

def search_students():
    for name, mark in students.items():
        print(f"{name} : {mark}")


while True:
    try:
        choice = int(input(f"1. Add Student\n"
                            "2. View Student\n"
                            "3. Search Student\n"
                            "4. Update Score\n"
                            "5. Delete Student\n"
                            "6. Exit\n"
                            "------------\n"
                            "Choose: "))
    except ValueError:
        print("Please Select Correct Choice")
        continue

    if choice == 1:
        student = input("Key In Student Name: ").capitalize()
        students[student] = 0

    elif choice == 2:
        search_students()

    elif choice == 3:
        search = input("Search Student Name: ").capitalize()
        if search in students:
            print("Have This Student")
        else:
            print("Not found")




