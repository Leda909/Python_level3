#Print welcome message
print("Welcome to a simple budgeting calculator")

budget = 0

#Main loop for the budeting program
while True:
  
  #Prompt the user to choose an action
  action = input("Enter 'i' to add income, 'e' to add expenses, 'v' to view financial summary, 'q' to quit")
  
  #Add income
  if action == "i":
    budget += int(input("Write the income that you want to add: "))
    print("Income successfully added")
  
  #Extract expenses  
  elif action == "e":
    budget -= int(input("Write the expenses that you want to add: "))
    print("Expenses successfully added")
  
  #Show the current budget
  elif action == "v":
    print(budget)
  
  #Quit the program  
  elif action == "q":
    print("Exiting program, goodbye!")
    break
    
  #Error handling incorrect inputs!
  else:
    print("Incorrect input, try again")
