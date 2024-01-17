world = ['Japan', 'Italy', 'Korea', 'Philippines', 'Paris'] #The "world" becomes a list with the 3 counntries 

print("\nAlphabetical:")
print(sorted(world)) #prints the list in a alphabetical order

print("\nOriginal order:")
print(world) #prints the list in its original order 

print("\nReverse alphabetical:")
print(sorted(world, reverse=True)) #prints the list in a alphabetical order but in reverse

print("\nOriginal order:")
world.reverse() #makes the list order reversed 
print(world) #prints the list in its original order

print("\nAlphabetical:")
world.sort() #sorts the list in order alphabetically
print(world) #prints the list in a alphabetical order

print("\nReverse alphabetical:")
world.sort(reverse=True) #reverse the list in orer
print(world) #prints the list in its original order but in reverse


