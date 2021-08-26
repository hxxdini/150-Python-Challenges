'''021 - Ask the user to enter their first name and then ask them to 
enter their surname. Join them together with a space between and display
the name and the length of whole name.'''

firstName = input("First Name: \n")
surName = input("Sur Name: \n")

fullName = firstName + " " + surName

print("Name:",fullName,"\nLength:",len(fullName))

