'''008 - Ask for the total price of the bill, then ask how many diners there are.
Divide the total bill by the number of diners and show how much each person must pay. '''

totalBill = int(input("What's the total price of the bill? \n"))
totalDiners = int(input("How many diners are in here? \n"))

splitBill = totalBill//totalDiners # A single / returns a float

print("The diners must pay $",splitBill,"each")

