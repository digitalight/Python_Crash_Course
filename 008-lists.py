ubuntu_distros = ['ubuntu', 'kubuntu', 'xubuntu', 'ubuntu mate', 'ubuntu studio', 'ubuntu budgie']
print(ubuntu_distros)
print(f"The first in the list is {ubuntu_distros[0].title()}")
print(f"The last in the list is {ubuntu_distros[-1].title()}")

# Append
ubuntu_distros.append('ubuntu server')
print(f"The last in the list is now {ubuntu_distros[-1].title()}")

# Insert
ubuntu_distros.insert(0, 'ubuntu cinnamon')
print(f"The first in the list is now {ubuntu_distros[0].title()}")

# Deleting
del ubuntu_distros[0]
print(f"The first in the list is now {ubuntu_distros[0].title()}")

# Popping
ubuntu_distros.append('ubuntu cinnamon')
popped_ubuntu = ubuntu_distros.pop()
print(f"List is now {ubuntu_distros}")
print(f"Popped: {popped_ubuntu}")

# Remove
print("Remove blah")
ubuntu_distros.insert(2,'blah')
print(ubuntu_distros)
ubuntu_distros.remove('blah')
print(ubuntu_distros)