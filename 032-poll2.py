# Making a dictionary for poll 
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for name
    name = input("\nWhat is your name? ")
    response = input("What mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Is someone else going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results
print("\nCompleted")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")