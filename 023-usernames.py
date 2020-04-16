users = {
    'jsmith': {
        'first': 'john',
        'last': 'smith',
        'location': 'uk',
    },
    'sdavies': {
        'first': 'sue',
        'last': 'davies',
        'location': 'usa',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")