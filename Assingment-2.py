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
    print("Enter your monthly expenses in category & Type 'Done' when you are done")
    while True:
       Category = input("Enter Category name: ")
       if Category == "Done":
         break  
       
       if Category not in expense:
        expense[Category] = []
       
        while True:   
            amount = (input("Enter amount for : "))
            if amount == "Next":
                break  
            try:
                amount = float(amount)
                expense[Category].append(amount)
            except ValueError:
               print("Invalid input. Please enter a valid number.")
               return expense

expense = Monthly_expenses()

