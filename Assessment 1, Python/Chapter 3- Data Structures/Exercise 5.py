guests = ['Jule', 'Chuchuy', 'Bam'] #"guests" becomes a list with 3 names 

name = guests[0].title() #"name" is placed in the first name from the list
print(f"{name}, would you like to go to the party later?") #prints the data inside the "name" with the statement in the same line

name = guests[1].title() #"name" is placed in the second name from the list
print(f"{name}, would you like to go to the party later?") #prints the data inside the "name" with the statement in the same line

name = guests[2].title() #"name" is placed in the third name from the list
print(f"{name}, would you like to go to the party later?") #prints the data inside the "name" with the statement in the same line

name = guests[1].title() #The "name" is placed in the second name from the list
print(f"\nThat's unfortunate, {name} said they can't come.") #prints the data placed in the "name" with the statement in the same line

del(guests[1]) #deletes the second name in the list
guests.insert(1, 'Chuchuy') #input a new name to replace the deleted name on the list

name = guests[0].title() ##The "name" is placed in the first name from the list
print(f"\{name}), would you like to go to thr paty later?") #prints the data inside the "name" with the statement in the same line

name = guests[1].title() #"name" is placed in the second name from the list
print(f"{name}, would you like to go to the party later?") #prints the data inside the "name" with the statement in the same line

name = guests[2].title() #"name" is placed in the third name from the list
print(f"{name}, would you like to go to the party later?") #prints the data inside the "name" with the statement in the same line