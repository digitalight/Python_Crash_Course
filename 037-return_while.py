def get_fullname(first, last):
    """Return a full name"""
    full_name = f"{first} {last}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name:  ")
    if l_name == 'q':
        break
    formatted_name = get_fullname(f_name, l_name)
    print(f"\nHello there, {formatted_name}!")