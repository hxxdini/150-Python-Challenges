'''012 - Ask for two numbers. If the first one is larger than the second,
display the second number first and then the first number,
otherwise show the first number first and then the second.'''

firstNumber = int(input("Enter first number:\n"))
secondNumber = int(input("Enter second number:\n"))

if firstNumber > secondNumber:
    print("Second number =",secondNumber,"& First number =",firstNumber)
else:
    print("First number =",firstNumber,"& Second Number =",secondNumber)
