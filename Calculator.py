FirstNumber = 0
Total = 1
while True:
    #checks to see if the first number is equal to the total to continue calculations after the loop
    if FirstNumber == Total:
        SecondNumber = input('Please enter another number: ')
        if SecondNumber.isnumeric() != True:
            print('Please enter a valid number') 
            continue
        Operation = input('Which operation would you like to complete (*,/,+,-): ')
        if Operation != '*' and Operation != '+' and Operation != '-' and Operation != '/':
            print('Please enter a valid operation')
            continue
        pass
    else:
        #inputs numbers and operations and returns back if invalid value has been inputed
        FirstNumber = input('Please enter your first number: ')
        if FirstNumber.isnumeric() != True:
            print('Please enter a valid number') 
            continue
        SecondNumber = input('Please enter your second number: ')
        if SecondNumber.isnumeric() != True:
            print('Please enter a valid number') 
            continue
        Operation = input('Which operation would you like to complete (*,/,+,-): ')
        if Operation != '*' and Operation != '+' and Operation != '-' and Operation != '/':
            print('Please enter a valid operation')
            continue
    #calculates the operation
    if Operation == '*':
        Total = float(FirstNumber) * float(SecondNumber)
    elif Operation == '/':
        if SecondNumber == '0':
            Total = 'Error: Cannot divide by zero'
        else:
            Total = float(FirstNumber) / float(SecondNumber)
    elif Operation == '+':
        Total = float(FirstNumber) + float(SecondNumber)
    elif Operation == '-':
        Total = float(FirstNumber) - float(SecondNumber)
    print(Total)
    #asks the user if they want to stop or continue calculating
    MultipleOperations = input('Would you like to perform another operation? (Yes or No): ').lower()
    if MultipleOperations == 'no':
        break
    elif MultipleOperations == 'yes':
        NewOperation = input('Would you like to start a new calculation or use exisiting calculation? (New or Exist): ').lower()
        if NewOperation == 'new':
            continue
        elif NewOperation == 'exist':
            FirstNumber = Total