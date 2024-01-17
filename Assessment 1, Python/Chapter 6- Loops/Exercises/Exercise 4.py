sandwhich_orders = ['Chicken','Tuna', 'Egg','Beef'] #"sandwhich_orders" turns into a list that has 4 items
finished_sandwiches = [] ##The "finished_sandwhiches" turns into the empty list

while sandwhich_orders: #while "sandwhich_orders" is true 
    curent_sandwich = sandwhich_orders.pop() #"curent_sandwhich" is placed in the retrived data in "sandwhich_order"
    print(f"Your {curent_sandwich} sandwhich is being made.") #prints the statement in the same line of stored in "curent_sandwhich"
    finished_sandwiches.append(curent_sandwich) #adds that data placed in "curent_sandwhich" to the list "finished_sandwhiches"

    print("\n")
    for sandwich in finished_sandwiches: 
        print(f"The {sandwich} sandwich is finished.") #prints the statement in this line and the words placed in the list of "finished_sanwiches"

        