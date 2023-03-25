import random
#Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
#creates a list from names_string
names = names_string.split(", ")
#calculating a random index number between 0 and length of names minus 1
#have to subtract 1 from length to account for zero based indexing
buyer = random.randint(0, len(names)-1)
#determining which name in the list is associated with the random index
banker = names[buyer]
#Telling everyone who gets to buy lunches today
print(f'{banker} is going to buy the meal today!')
