'''015 - Ask the user to enter their favourite colour. If they enter “red”, “RED” or 
“Red” display the message “I like red too”, otherwise display the message 
“I don’t like [colour], I prefer red”.'''

favoriteColor = input("What's your favorite color?\n")

if favoriteColor == 'red' or favoriteColor == 'RED' or favoriteColor == 'Red':
    print("I like red too")
else:
    print(f"I don't like {favoriteColor}, I prefer red")
