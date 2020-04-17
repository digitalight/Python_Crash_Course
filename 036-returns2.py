# Return in a dictionary format
def build_persion(first, last, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    return person

musician = build_persion('louis', 'armstrong', age=69)
print(musician)