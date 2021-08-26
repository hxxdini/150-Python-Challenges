'''009 - Write a program that will ask for a number of days 
and then will show how many hours, minutes and seconds are 
in that number of days.'''


days = int(input("Enter any number of days:\n"))
hours = days*24
minutes = hours*60
seconds = minutes*60

print("There are,",hours,"hours,",minutes,"minutes and",seconds,"seconds in",days,"day(s).")


