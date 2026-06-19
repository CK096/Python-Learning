task_list =[]

while True:
    try:
        choice = int(input("1.Add Task\n"
                           "2.View Task\n"
                           "3.Remove Task\n"
                           "4.Mark Completed\n"
                           "5.Undo Mark\n"
                           "6.Exit\n"
                           "------------\n"
                           "Choose: "))
    except ValueError:
        print("Invalid")
        continue

    if choice == 1:
        quest = input("Enter Task: ")
        task_list.append({"task": quest, "done": False})
        print("Task Added!\n------------")
    elif choice == 2:
        if not task_list:
            print("No Task Found!")
            continue
        for x, y in enumerate(task_list):
            if y["done"]:
                print(f'{x+1}. [✓] {y["task"]}')
            else:
                print(f'{x+1}. [ ] {y["task"]}')
    elif choice == 3:
        if not task_list:
            print("No Task Found!")
            continue
        try:
            delete = int(input("Select Task You Want To Remove: "))
        except ValueError:
            print("Invalid")
            continue
        if not 1 <= delete <= len(task_list):
            print(f"Dont have {delete}, please choice again! ")
            continue
        del task_list[delete-1]
        print("Task Removed!\n------------")
        for x, y in enumerate(task_list):
            if y["done"]:
                print(f'{x+1}. [✓] {y["task"]}')
            else:
                print(f'{x+1}. [ ] {y["task"]}')
    elif choice == 4:
        if not task_list:
            print("No Task Found!")
            continue
        for x, y in enumerate(task_list):
            if y["done"]:
                print(f'{x+1}. [✓] {y["task"]}')
            else:
                print(f'{x+1}. [ ] {y["task"]}')
        try:
            mark = int(input("Please Mark what task is complete: "))
        except ValueError:
            print("Invalid")
            continue
        if not 1 <= mark <= len(task_list):
            print("Wrong Key In!")
            continue
        if task_list[mark-1]["done"]:
            print("Already complete")
        else:
            task_list[mark-1]["done"] = True
            for x, y in enumerate(task_list):
                if y["done"]:
                    print(f'{x + 1}. [✓] {y["task"]}')
                else:
                    print(f'{x + 1}. [ ] {y["task"]}')
    elif choice == 5:
        for x, y in enumerate(task_list):
            if y["done"]:
                print(f'{x + 1}. [✓] {y["task"]}')
            else:
                print(f'{x + 1}. [ ] {y["task"]}')
        try:
            undo = int(input("Key In Mark you want to Undo: "))
        except ValueError:
            print("Invalid")
            continue
        if not 1 <= undo <= len(task_list):
            print("Wrong Key In!")
            continue
        if task_list[undo-1]["done"]:
            task_list[undo-1]["done"] = False
            print("Mark Cancelled!")
        else:
            print("Task is No Complete!")
        for x, y in enumerate(task_list):
            if y["done"]:
                print(f'{x+1}. [✓] {y["task"]}')
            else:
                print(f'{x+1}. [ ] {y["task"]}')
    elif choice == 6:
        break
