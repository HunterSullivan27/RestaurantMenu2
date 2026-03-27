print("Hello! Welcome to Sullivan's Salads.")
drink_price = 0
order_prices = []
order_summaries = []

keep_ordering = True
order_num = 0
while keep_ordering:
    order_num += 1
    order_choices = []
    # Protein
    protein_order_complete = False
    while not protein_order_complete:
        protein_choice = input("What kind of protein would you like in your salad? Chicken, steak, or tofu? Please make sure to answer in all lowercase.")
        if protein_choice == "chicken":
            order_prices.append(5.99)
            protein_order_complete = True
        elif protein_choice == "steak":
            order_prices.append(7.99)
            protein_order_complete = True
        elif protein_choice == "tofu":
            order_prices.append( 6.99)
            protein_order_complete = True
        else:
            print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
    print(f"Great! That will be {order_prices[-1]}")
    order_choices.append(protein_choice)

    # Dressing
    dressing_order_complete = False
    while not dressing_order_complete:
        dressing_yes_or_no = input("Would you like dressing on that?")
        if dressing_yes_or_no == "yes":
            dressing_choice = input("What kind of dressing? We have ranch, balsamic, and italian.")
            if dressing_choice == "ranch":
                order_prices.append( 0.5)
                print("Good choice! That'll be 2 nickels.")
                dressing_order_complete = True
            elif dressing_choice == "balsamic":
                order_prices.append( 0.25)
                print("My favorite! That'll be an additional 25 cents.")
                dressing_order_complete = True
            elif dressing_choice == "italian":
                order_prices.append( 1)
                print("Okay! That'll be $1.")
                dressing_order_complete = True
            else:
                print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
        elif dressing_yes_or_no == "no":
            order_prices.append(0)
            print("Too bad, so sad!")
            dressing_order_complete = True
            dressing_choice = "no"
        else:
            print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
    order_choices.append(dressing_choice)

    # Drink
    # TODO: migrate to order_prices.append(???) instead of drink_price = ???
    drink_order_complete = False
    while not drink_order_complete:
        drink_yes_or_no = input("Would you like a drink? (yes or no)")    
        if drink_yes_or_no == "yes":
            drink_choice = input("What kind of drink would you like? We have water, Coke Zero, and coffee. Please make sure to answer in all lowercase.")
            if drink_choice == "water":
                print("Great! That will be complimentary")
                drink_order_complete = True
            elif drink_choice == "coke zero":
                order_prices.append (2)
                print("Great! That will be $2")
                drink_order_complete = True
            elif drink_choice == "coffee":
                order_prices.append (4)
                print("Great! That will be $4")
                drink_order_complete = True
            else:
                print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
        elif drink_yes_or_no == "no":
            order_prices.append (0)
            print("Your loss!")
            drink_order_complete = True
            drink_choice = "nothing"
        else:
            print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
    order_choices.append(drink_choice)

    # Croutons
    crouton_count_complete = False
    crouton_count = 0
    while not crouton_count_complete:
        crouton_yes_or_no = input("Would you like croutons?")
        if crouton_yes_or_no == "yes":
            # NOTE: this may throw an exception if user enters a non-number
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
    order_choices.append(crouton_count)
    order_prices.append(crouton_count * 0.25)
    drink_order_complete = True
    # TODO: print order up until now
    summary = f"Order #{order_num} is a {order_choices[0]} salad with {order_choices[1]} dressing, and {order_choices[2]} to drink. Along with {order_choices[3]} croutons."
    order_summaries.append(summary)
    user_input = input("Would you like to order more? [yes/no]")
    if user_input == "yes":
        keep_ordering = True
    else:
        keep_ordering = False

total_cost = sum(order_prices)

# TODO: use the order_choices list to access each salad option...
for summary in order_summaries:
    print(summary)

subtotal = f"Subtotal: ${total_cost}"
print(subtotal)
print(f"Total Price (w/tax): ${total_cost * 1.08:.2f}")
