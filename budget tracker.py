#Personal Budget Tracker

incomes = []
expenses = []
number_of_incomes = int(input("How many incomes do you have? ", ))
number_of_expenses = int(input("How many expenses do you have? "))
for i in range(number_of_incomes):
    description_i = input("description of income ",)
    category_i = input("category of income ",)
    amount_i = int(input("amount of income ",))
    date_i = input("date in format dd/mm/yyyy ",)

    income_dict = {
        "description": description_i,
        "category": category_i,
        "amount": amount_i,
        "date": date_i

    }
    incomes.append(income_dict)
for e in range(number_of_expenses):
    description_e = input("description of expense ")
    category_e = input("description of category ")
    amount_e = int(input("amount of expense "))
    date_e = input("date in format dd/mm/yyyy")

    expense_dict = {
        "description" : description_e,
        "category" : category_e,
        "amount" : amount_e,
        "date" : date_e
    }
    expenses.append(expense_dict)


        

transactions = input("view all transactions or transaction by date, category,type(income or expenses) or balances: ")

if transactions == "date":
    day_of_transactions = input("enter date in format dd/mm/yyyy: ")
    for income in incomes:          
        if  income["date"] == day_of_transactions:
            print("description: " ,income["description"])
            print("category: ", income["category"])
            print("amount: ", income["amount"])
            print("date: ", income["date"])
            print(" ")
    for expense in expenses:
        if expense["date"] == day_of_transactions:
            print("description: " ,expense["description"])
            print("category: ", expense["category"])
            print("amount: ", expense["amount"])
            print("date: ", expense["date"])
            print(" ")

elif transactions == "category":
    category_to_filter_out = input("enter the category you would like to filter out: ")
    for income in incomes:          
        if  income["category"] == category_to_filter_out:
            print("description: " ,income["description"])
            print("category: ", income["category"])
            print("amount: ", income["amount"])
            print("date: ", income["date"])
            print(" ")
    for expense in expenses:
        if expense["category"] == category_to_filter_out:
            print("description: " ,expense["description"])
            print("category: ", expense["category"])
            print("amount: ", expense["amount"])
            print("date: ", expense["date"])
            print(" ")

elif transactions == "type":
    transaction_type = input("please enter the transaction type (incomes/expenses): ")
    for income in incomes:
        if transaction_type == "incomes":
            print("description: " ,income["description"])
            print("category: ", income["category"])
            print("amount: ", income["amount"])
            print("date: ", income["date"])
            print(" ")
    for expense in expenses:
        if transaction_type == "expenses":
            print("description: " ,expense["description"])
            print("category: ", expense["category"])
            print("amount: ", expense["amount"])
            print("date: ", expense["date"])
            print(" ")

elif transactions == "view all transactions":
    for income in incomes:
        print("description: " ,income["description"])
        print("category: ", income["category"])
        print("amount: ", income["amount"])
        print("date: ", income["date"])
        print(" ")
    for expense in expenses:
        print("description: " ,expense["description"])
        print("category: ", expense["category"])
        print("amount: ", expense["amount"])
        print("date: ", expense["date"])
        print(" ")

elif transactions == "balances":
    balances = input("view total income or total expenses or balances? ")
    if balances == "total income":
        total_income = 0
        for income in incomes:
            total_income = total_income + income["amount"]
        print("total income for this period is :", total_income)

    elif balances == "total expenses":
        total_expenses = 0
        for expense in expenses:
            total_expenses = total_expenses + expense["amount"]
        print("total expenses for this period is :",total_expenses)

    elif balances == "balances":
        total_income = 0
        total_expenses = 0
        for income in incomes:
            total_income = total_income + income["amount"]
        for expense in expenses:
            total_expenses = total_expenses + expense["amount"]
        balance = total_income - total_expenses
        print("the balance amount for this period is :", balance)
else:
    print("please enter a valid prompt 'view all transactions' or 'date' or 'category' or 'type'")
