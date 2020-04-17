# All about different ways of passing arguments to functions.

# Positional Arguments
def describe_friend(friend_name, friend_gender, friend_age):
    """Display info about a friend"""
    print(f"\nI have a friend called {friend_name.title()}.")
    print(f"{friend_name.title()} is a {friend_age} year old {friend_gender.lower()}.")

describe_friend('bob', 'male', 32)

# Keyword Arguments
# def describe_friend(friend_name, friend_gender, friend_age):
#     """Display info about a friend"""
#     print(f"\nI have a friend called {friend_name.title()}.")
#     print(f"{friend_name.title()} is a {friend_age} year old {friend_gender.lower()}.")

describe_friend(friend_name='susan', friend_gender='female', friend_age=62)

# Default Values

def describe_pet(pet_name, animal_type='dog'):
    """Display information about the pet"""
    print(f"\nI have a {animal_type}, called {pet_name.title()}.")
describe_pet(pet_name='sam')