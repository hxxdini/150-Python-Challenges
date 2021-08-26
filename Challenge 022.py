'''023 - Ask the user to type in the first line of a nursery rhyme and display the length of the string. 
Ask for a starting number and an ending number and then display just that section of the text
(remember Python starts counting from 0 and not 1).'''

nurseryRhyme = input("Type the first line of a nursery rhyme\n...")

print("This nursery rhyme line is",len(nurseryRhyme),"characters long\n")

start = int(input("Type a starting number ..\n"))
end = int(input("Type the ending number ..\n"))

print(nurseryRhyme[start:end],"\n")



