'''## Exercise 5: Favorite Fruit :ballot_box_with_check:

Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

•Make a list of your three favorite fruits and call it favorite_fruits.

•Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block 

should print a statement,such as You really like bananas!'''

fav_fruits = ["mango","banana","persimmon"]
fav_fruits[0] = "apple"

if "persimmon" in fav_fruits:
    print("You really like persimmon!")
elif "apple" in fav_fruits:
    print("You really like apples!")
elif "grapes" in fav_fruits:
    print("You really like grapes")
elif"strawberry" in fav_fruits:
    print("You really like strawberries!")
elif"banana" in fav_fruits: 
    print("You really like bananas!")


