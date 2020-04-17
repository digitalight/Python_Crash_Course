# undefined number of arguments is *
# put this at the end and fix position ones go at the beginning

def make_pizza(size, *toppings):
    """Print out list of toppings"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')