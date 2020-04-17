# Start with users that need verifying and an empty list of confirmed
unconfirmed_users = ['alice', 'brian', 'john']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into confirm_user

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\n The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

