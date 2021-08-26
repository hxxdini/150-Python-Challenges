'''018 - Ask the user to enter a number. If it is under 10, display the message “Too low”,
if their number is between 10 and 20, display “Correct”, otherwise display “Too high”.'''

randomNumber = int(input("Enter a random number:\n"))

if randomNumber < 10:
    print("Too low")
elif randomNumber >= 10 and randomNumber <= 20:
    print("Correct")
else:
    print("Too high")


