students = {}

def search_students():
    for name, mark in students.items():
        print(f"{name} : {mark}")
    print("------------")

def no_rekod_student():
    if not students:
        print("Rekod Is Empty!")
        return True

def not_found_student(name):
    if name not in students:
        print("This Student Name Invalid!")
        return True

def error_key(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid")


while True:
    try:
        choice = int(input(f"1. Add Student\n"
                            "2. View Student\n"
                            "3. Search Student\n"
                            "4. Update Score\n"
                            "5. Delete Student\n"
                            "6. Exit\n"
                            "\n"
                            "Choose: "))
    except ValueError:
        print("Please Select Correct Choice")
        continue

    if choice == 1:
        student = input("Key In Student Name: ").capitalize()
        if student in students:
            print("Student Already Exists")
            continue
        elif student.strip() == "":
            continue
        students[student] = 0


    elif choice == 2:
        if no_rekod_student():
            continue
        search_students()

    elif choice == 3:
        if no_rekod_student():
            continue
        search = input("Search Student Name: ").capitalize()
        if not_found_student(search):
            continue
        if search in students:
            print("Have This Student")

    elif choice == 4:
        if no_rekod_student():
            continue
        search_students()
        name = input("Select Student: ").capitalize()
        if not_found_student(name):
            continue
        score = error_key(("Update Student Score: "))
        if 0 > score or score > 100:
            print("Score minimun is 0 and maximun is 100 ")
            continue
        students.update({name:score})
        print(f"Update {name} Score Complete")

    elif choice == 5:
        if no_rekod_student():
            continue
        search_students()
        delete = input("Select student U want delete: ").capitalize()
        if not_found_student(delete):
            continue
        del students[delete]
        print("Student Rekod Is Delete!!!")

    elif choice == 6:
        print("Thanks For Using")
        break







