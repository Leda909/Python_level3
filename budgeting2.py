#Welcome message, display a menu of options; adding income, adding expense, viewing financial summary, quitting the program
#users should be able to add both incomes and expenses separetly
#the financial summary should display the total income, total expenses, and the remaining balance after deducting expenses from income

#Print welcome message
print("Welcome to the Simple Budgeting Calculator")

total_incomes = 0
total_expenses = 0

#Main loop for the budeting program
while True:
  
  #Prompt the user to choose an action
  action = input("Enter 'i' to add income, 'e' to add expenses, 'v' to view financial summary, 'q' to quit")
  
  #Add income
  if action == "i":
    total_incomes += int(input("Write the income that you want to add: "))
    print("Income successfully added")
  
  #Add expenses  
  elif action == "e":
    total_expenses += int(input("Write the expenses that you want to add: "))
    print("Expenses successfully added")
  
  #Show the financial summary: display the total income, total expenses, and the remaining balance after deducting expenses from income
  elif action == "v":
    # Respond in one line
    # print(f"The financial summary: Total income: {total_incomes} - Total expense: {total_expenses} = The remaining balance:  {total_incomes - total_expenses}")
    print("The financial summary:")
    print(f"Income: {total_incomes}")
    print(f"Expenses: {total_expenses}")
    print(f"The remaining balance:  {total_incomes - total_expenses}")
  
  #Quit the program  
  elif action == "q":
    print("Exiting program, goodbye!")
    break
    
  #Error handling incorrect inputs!
  else:
    print("Incorrect input, try again")
