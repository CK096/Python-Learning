def load_expense():
    try:
        with open(path_file, "r") as file:
            for line in file:
                data = line.strip().split(",")
                category = data[0]
                amount = float(data[1])
                expenses.append({"category": category,"amount": amount})
    except FileNotFoundError:
        pass

def save_expense():
    with open(path_file,"w") as file:
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']}\n")

def view_expense():
    for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense['category']} : RM {expense['amount']:.2f}")
def empty_expense():
    if not expenses:
        print("Expenses record is empty!!")
        return True
    return False

def negative_amount(amount):
    if amount < 0:
        print("Amount cannot less then 0 !")
        return True
    return False

def category_empty(category):
    if not category:
        print("Category cannot be empty!")
        return True
    return False

def error_key(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid Number")
def error_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Number")

expenses = []
path_file = r"C:\Users\user\Desktop\workshop\expenses_record.txt"
load_expense()

while True:
    choice = error_key("=====Expense Tracker=====\n"
                       "1.Add Expense\n"
                       "2.View Expense\n"
                       "3.Search Expense\n"
                       "4.Delete Expense\n"
                       "5.Total Expense\n"
                       "6.Category Summary\n"
                       "7.Edit Category\n"
                       "8.Exit\n"
                       "-------------------------\n"
                       "Choice :")
    if choice == 1:
        print("=====Add Tracker=====")
        category = input("Type Of Category Expense:").strip().title()
        if category_empty(category):
            continue
        amount = error_float("How Many you use?: RM ")
        if negative_amount(amount):
            continue
        expenses.append({"category": category, "amount": amount})
        print("Add in Success!")

        save_expense()
    elif choice == 2:
        if empty_expense():
            continue
        print("=====Expense Tracker=====")
        empty_expense()
        view_expense()
    elif choice == 3:
        found = False
        if empty_expense():
            continue
        search = input("what category expense you want to search: ").strip().title()
        for index,result in enumerate(expenses):
            if result["category"] == search:
                found = True
                print(f"{index + 1}.{result['category']} RM {result['amount']:.2f}")
        if not found:
            print("Category Not Found")

    elif choice == 4:
        if empty_expense():
            continue
        print("=====Delete Tracker=====")
        view_expense()
        delete = error_key("Select list item need to remove: ")
        if delete < 1 or delete > len(expenses):
            print("Invalid")
            continue
        del expenses[delete - 1]
        print("Item list remove Success")
        save_expense()
    elif choice == 5:
        if empty_expense():
            continue
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print(f"Total is RM {total:.2f}")

    elif choice == 6:
        if empty_expense():
            continue
        summary = {}
        print("===== Category Summary =====")
        for expense in expenses:
            if expense["category"] in summary:
                summary[expense["category"]] += expense["amount"]
            else:
                summary[expense["category"]] = expense["amount"]
        for category,price in summary.items():
            print(f"{category} : RM {price:.2f}")

    elif choice == 7:
        if empty_expense():
            continue
        print("===== Edit Expense =====")
        view_expense()
        edit = error_key("Select expense number: ")
        if edit > len(expenses) or edit < 1:
            print("This Number Invalid")
            continue
        print(f"Current Category : {expenses[edit-1]["category"]}")
        print(f"Current Amount : RM {expenses[edit-1]["amount"]:.2f}")
        new_category = input("New Category: ").strip().title()
        if category_empty(new_category):
            continue
        expenses[edit-1]["category"] = new_category
        new_amount = error_float("New Amount: RM ")
        if negative_amount(new_amount):
            continue
        expenses[edit - 1]["amount"] = new_amount
        print(f"Update Success!\n "
              f"Category: {expenses[edit-1]["category"]}\n"
              f"Amount: RM {expenses[edit-1]["amount"]:.2f})")
        save_expense()

    elif choice == 8:
        print("Thanks for using Expense Traker")
        break
