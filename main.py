print("Hello! Welcome to Sullivan's Salads.")
protein_order_complete = False
while not protein_order_complete:
    protein_choice = input("What kind of protein would you like in your salad? Chicken, beef, or tofu? Please make sure to answer in all lowercase.")
    if protein_choice == "chicken":
        protein_price = 5.99
        print("Great! That will be $5.99")
        protein_order_complete = True
    elif protein_choice == "beef":
        protein_price = 7.99
        print("Great! That will be $7.99")
        protein_order_complete = True
    elif protein_choice == "tofu":
        protein_price = 6.99
        print("Great! That will be $6.99")
        protein_order_complete = True
    else:
        print("Sorry! There was an error with your input. Check to make sure you selected a valid option and answered in all lowercase.")
protein_order_complete = True
