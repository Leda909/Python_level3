#Print welcome message
print("Welcome to the Simple Budgeting Calculator")

incomes = []
expenses = []

#Main loop for the budeting program
while True:
  
  #Prompt the user to choose an action
  action = input("Enter 'i' to add income, 'e' to add expenses, 'v' to view financial summary, 'q' to quit")
  
  #Add income
  if action == "i":
    income = float(input("Write the income that you want to add: "))
    incomes.append(income)
    print("Income successfully added")
  
  #Add expenses  
  elif action == "e":
    expense = float(input("Write the expenses that you want to add: "))
    expenses.append(expense)
    print("Expenses successfully added")
  
  #Show the financial summary: display the total income, total expenses, and the remaining balance after deducting expenses from income
  elif action == "v":
    total_incomes = sum(incomes)
    total_expenses = sum(expenses)
    remaining_balance = total_incomes - total_expenses
    
    print("The Financial Summary:")
    print(f"Total Income: £{total_incomes}")
    print(f"Total Expenses: £{total_expenses}")
    print(f"Remaining balance:  £{remaining_balance}")
  
  #Quit the program  
  elif action == "q":
    print("Exiting program, goodbye!")
    break
    
  #Error handling for incorrect inputs!
  else:
    print("Incorrect input, try again")
