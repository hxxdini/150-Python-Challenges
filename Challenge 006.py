'''006 - Ask how many slices of pizza the user started with and ask 
how many slices they have eaten. 
Work out how many slices they have left and display the answer in a
userfriendly format.'''

startSlices = int(input("How many slices of pizza did you start with?\n"))
slicesEaten = int(input("How many slices have you eaten?\n"))

slicesLeft = startSlices - slicesEaten

print("There are",slicesLeft,"slices of Pizza left.")
