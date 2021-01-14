def sandwich_toppings(*toppings):
    """Prints a summary of all the sandwich toppings"""
    print("Your sandwich will have the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")


sandwich_toppings('salami', 'ham', 'bacon')
