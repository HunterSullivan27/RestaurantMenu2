print("Hello! Welcome to Sullivan's Salads.")
protein_price = 0
drink_price = 0
protein_order_complete = False
while not protein_order_complete:
    protein_choice = input("What kind of protein would you like in your salad? Chicken, steak, or tofu? Please make sure to answer in all lowercase.")
    if protein_choice == "chicken":
        protein_price = 5.99
        print("Great! That will be $5.99")
        protein_order_complete = True
    elif protein_choice == "steak":
        protein_price = 7.99
        print("Great! That will be $7.99")
        protein_order_complete = True
    elif protein_choice == "tofu":
        protein_price = 6.99
        print("Great! That will be $6.99")
        protein_order_complete = True
    else:
        print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
dressing_order_complete = False
while not dressing_order_complete:
    dressing_yes_or_no = input("Would you like dressing on that?")
    if dressing_yes_or_no == "yes":
        dressing_choice = input("What kind of dressing? We have ranch, balsamic, and italian.")
        if dressing_choice == "ranch":
            dressing_price = 0.5
            print("Good choice! That'll be 2 nickels.")
            dressing_order_complete = True
        elif dressing_choice == "balsamic":
            dressing_price = 0.25
            print("My favorite! That'll be an additional 25 cents.")
            dressing_order_complete = True
        elif dressing_choice == "italian":
            dressing_price = 1
            print("Okay! That'll be $1.")
            dressing_order_complete = True
        else:
            print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
    elif dressing_yes_or_no == "no":
        dressing_price = 0
        print("Too bad, so sad!")
        dressing_order_complete = True
        dressing_choice = "no"
    else:
        print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
drink_order_complete = False
while not drink_order_complete:
    drink_yes_or_no = input("Would you like a drink? (yes or no)")    
    if drink_yes_or_no == "yes":
        drink_choice = input("What kind of drink would you like? We have water, Coke Zero, and coffee. Please make sure to answer in all lowercase.")
        if drink_choice == "water":
            drink_price = 0
            print("Great! That will be complimentary")
            drink_order_complete = True
        elif drink_choice == "coke zero":
            drink_price = 2.00
            print("Great! That will be $2")
            drink_order_complete = True
        elif drink_choice == "coffee":
            drink_price = 4.00
            print("Great! That will be $4")
            drink_order_complete = True
        else:
            print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
    elif drink_yes_or_no == "no":
        drink_price = 0
        print("Your loss!")
        drink_order_complete = True
        drink_choice = "nothing"
    else:
        print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
crouton_count_complete = False
while not crouton_count_complete:
    crouton_yes_or_no = input("Would you like croutons?")
    if crouton_yes_or_no == "yes":
        crouton_count = int(input("Great! How many would you like? It's 25 cents per crouton.").strip())
        if crouton_count > 10:
            print("Sorry! We can't give you anymore than 10.")
            crouton_count = 10
            crouton_count_complete = True
        elif crouton_count <= 10:
            print("Okay great!")
            crouton_count_complete = True
        else:
            print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
    elif crouton_yes_or_no == "no":
        print("Okay!")
        crouton_count_complete = True
    else: 
        print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
crouton_price = crouton_count * 0.25
drink_order_complete = True
peanut_order_complete = False
total_cost = protein_price + drink_price + dressing_price + crouton_price
result = f"Your final order is a {protein_choice} salad with {dressing_choice} dressing, and {drink_choice} to drink. Along with {crouton_count} croutons."
print(result)
subtotal = f"Subtotal: ${total_cost}"
print(subtotal)
print(f"Total Price: ${total_cost * 1.08:.2f}")