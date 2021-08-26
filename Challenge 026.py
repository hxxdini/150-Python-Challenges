'''026 - Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an 
“ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay, 
banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the 
user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case.'''

word = input("Enter a random word below\n... ")
word = word.lower()

if word[0] != "a" and word[0] != "e" and word[0] != "i" and word[0] != "o" and word[0] != "u":
    newWord = word[1:len(word)]+word[0]+"ay"
    print(newWord.lower())
else:
    print(word+"way")


