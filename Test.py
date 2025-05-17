def Welcome_message():
    print("Enter you name: ")
    name = input()
    print("Welcome to Your Budget Tracker " + name + "!")
    return name
    
name = Welcome_message()

def Monthly_income():
    print("Enter your monthly income: ")
    monthly_income = float(input())
    return monthly_income

income = Monthly_income()

def Monthly_expenses():
    expense = {}
    print("Enter your monthly expenses & Type 'Done' when you are done")
    while True:
       item = input("Enter item name: ")
       if item == "Done":
         break
       try:
          amount = float(input("Enter amount: "))
          expense[item] = amount
       except ValueError:
          print("Invalid input. Please enter a valid number.")
    return expense


expense = Monthly_expenses()
total_expense = sum(expense.values())
balance = income - total_expense


def summary():
    print("You monthly income " + str(name) + " is RM" + str(income))
    print("You monthly expenses " + str(name) + " are RM" + str(total_expense))
    print("You monthly balance " + str(name) + " is RM" + str(balance))

summary()

def advice():
   if balance > 0:
       print("You saved RM" + str(balance) + " this month.keep it up!")
   elif balance == 0:
       print("You broke even. Try to save next month.")
   else:
      print("You overspent by RM" + str(abs(balance)) + " Cut some expenses")

advice()

