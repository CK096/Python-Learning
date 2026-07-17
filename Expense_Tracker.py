expenses = []
path_file = r"C:\Users\user\Desktop\workshop\expenses_record"

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
    expenses.append({"category" : category, "amount": amount})

def view_expense():
    for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense['category']} RM {expense['amount']:.2f}")


while True:
    load_expense()
    view_expense()
    add_expense()
    save_expense()
