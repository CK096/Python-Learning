def load_expense():
    try:
        with open(path_file, "r") as file:
            for line in file:
                data = line.strip().split(",")
                category = data[0]
                amount = float(data[1])
                expenses.append({"category": category,"amount" : amount})
    except FileNotFoundError:
        pass

def save_expense():
    with open(path_file,"w") as file:
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']}\n")

def add_expense():
    category = input("Type Of Category Expense:").strip().title()
    amount = float(input("How Many you use?: RM "))
    expenses.append({"category": category, "amount": amount})
    print("Add in Success!")

def view_expense():
    for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense['category']} : RM {expense['amount']:.2f}")

def error_key(prompt):
    while True:
        try:
            return int(input(prompt))
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
                       "6.Exit\n"
                       "-------------------------\n"
                       "Choice :")
    if choice == 1:
        add_expense()
        save_expense()
    elif choice == 2:
        view_expense()
    elif choice == 3:
        found = False
        search = input("what category expense you want to search: ").strip().title()
        for index,result in enumerate(expenses):
            if result["category"] == search:
              found = True
              print(f"{index + 1}.{result['category']} RM {result['amount']:.2f}")
        if not found:
            print("Category Not Found")

    elif choice == 4:
        view_expense()
        delete = error_key("Select list item need to remove: ")
        if delete < 1 or delete > len(expenses):
            print("Invalid")
            continue
        del expenses[delete - 1]
        print("Item list remove Success")
        save_expense()
    elif choice == 5:
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print(f"Total is RM {total:.2f}")

    elif choice == 6:
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
        print("Thanks for using Expense Traker")
        break
