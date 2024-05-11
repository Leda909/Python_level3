#Print welcome message
print("Welcome to the Financial Tracker!")

incomes = []
expenses = []

#Main loop for the budeting program
while True:
  
  #Prompt the user to choose an action
  print("Please choose an option:")
  print("1. Add an income")
  print("2. Add an expense")
  print("3. View financial summary")
  print("4. Quit")

  choice = input("Enter your choice: ")
  
  #Add income
  if choice == "1":
    income = float(input("Enter the amount of income: "))
    incomes.append(income)
    print("Income successfully added")
  
  #Add expenses  
  elif choice == "2":
    expense = float(input("Enter the amount of expense: "))
    expenses.append(expense)
    print("Expense successfully added")
  
  #Show the financial summary: display the total income, total expenses, and the remaining balance after deducting expenses from income
  elif choice == "3":
    total_incomes = sum(incomes)
    total_expenses = sum(expenses)
    remaining_balance = total_incomes - total_expenses
    
    print("The Financial Summary:")
    print(f"Total Income: £{total_incomes}")
    print(f"Total Expenses: £{total_expenses}")
    print(f"Remaining balance:  £{remaining_balance}")
  
  #Quit the program  
  elif choice == "4":
    print("Thank you for using the Financial Tracker. Goodbye!")
    break
    
  #Error handling for incorrect inputs!
  else:
    print("Invalid choice. Please enter a number between 1 and 4.")
