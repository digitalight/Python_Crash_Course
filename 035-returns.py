def get_full_name(first, last):
    """Returns a full name, formatted"""
    full_name = f"{first} {last}"
    return full_name.title()

musician = get_full_name('david', 'gilmore')
print(musician)

def get_full_name2(first, last, middle=''):
    """Returns a full name, formatted"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

musician = get_full_name2('john', 'hooker', 'lee')
print(musician)