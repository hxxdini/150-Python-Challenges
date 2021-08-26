'''005 - Ask the user to enter three numbers. Add together the first two numbers and then multiply 
this total by the third. Display the answer as
The answer is [answer].'''

firstNumber = int(input("Enter First Number: "))
secondNumber = int(input("Enter Second Number: "))
thirdNumber = int(input("Enter Third Number: "))

answer = ((firstNumber + secondNumber)*thirdNumber)

print("The answer is:",answer)
