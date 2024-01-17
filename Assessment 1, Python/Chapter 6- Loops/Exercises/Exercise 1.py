#The variables is given the statements for this propmt, +- will make both variables show in the terminal
propmt = "\n what topping would you like on your pizza?"
propmt += "\ Enter 'quit' when you're done:"

#The while loop becomes true 

while True:
    topping = input(propmt)
    #This prints the variable and the used has to inout their toppings
    if topping != 'quit': 
        #if the user inputs their answer that is not 'quit'
        print (f"The {topping} are now added on your pizza")
    #This prints the tring and the topping of the used's choice 
    else: 
        break 
    #This ends the code when the used input 'quit'