task_list =[]

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid")


def view_task_list():
    for x, y in enumerate(task_list):
        if y["done"]:
            print(f'{x + 1}. [✓] {y["task"]}')
        else:
            print(f'{x + 1}. [ ] {y["task"]}')

def empty_task_list():
    if not task_list:
        print("No Task Found!")
        return True
    return False

def quest_task_list(quest):
    task_list.append({"task": quest, "done": False})
    print("Task Added!\n------------")

def remove_task_list(delete):
    if not 1 <= delete <= len(task_list):
        print(f"Dont have {delete}, please choice again! ")
        return True
    del task_list[delete - 1]
    print("Task Removed!\n------------")

def mark_task_list(mark):
    if not 1 <= mark <= len(task_list):
        print("Wrong Key In!")
        return True
    if task_list[mark - 1]["done"]:
        print("Already complete")
    else:
        task_list[mark - 1]["done"] = True

def undo_task_list(undo):
    if not 1 <= undo <= len(task_list):
        print("Wrong Key In!")
        return True
    if task_list[undo-1]["done"]:
        task_list[undo-1]["done"] = False
        print("Mark Cancelled!")
    else:
        print("Task is No Complete!")

while True:
    choice = get_number("1.Add Task\n"
                       "2.View Task\n"
                       "3.Remove Task\n"
                       "4.Mark Completed\n"
                       "5.Undo Mark\n"
                       "6.Exit\n"
                       "------------\n"
                       "Choose: ")

    if choice == 1:
        quest = input("Enter Task: ")
        quest_task_list(quest)
    elif choice == 2:
        if empty_task_list():
            continue
        view_task_list()
    elif choice == 3:
        if empty_task_list():
            continue
        view_task_list()
        delete = get_number("Select Task You Want To Remove: ")
        remove_task_list(delete)
        if not task_list:
            print("No Task List Now!")
        else:
            view_task_list()
    elif choice == 4:
        if empty_task_list():
            continue
        view_task_list()
        mark = get_number("Please Mark what task is complete: ")
        mark_task_list(mark)
        view_task_list()
    elif choice == 5:
        if empty_task_list():
            continue
        view_task_list()
        undo = get_number("Key In Mark you want to Undo: ")
        undo_task_list(undo)
        view_task_list()
    elif choice == 6:
        break
