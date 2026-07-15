expenses = []

def add_expense():
    category = input("Type Of Category Expense:").strip().title()
    amount = float(input("How Many you use?: RM "))
    expenses.append({"category" : category, "amount": amount})

def view_expense():
    for index, expense in enumerate(expenses):
        print(f"{index+1}. {expense.get('category')} RM {expense.get('amount'):.2f}")


while True:
    add_expense()
    view_expense()
