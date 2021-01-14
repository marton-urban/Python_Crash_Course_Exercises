# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pets = {
    'john': {
        'animal type': 'python',
        'owner': 'guido',
        'weight': 43,
        'eats': 'bugs',
    },
    'clarence': {
        'animal type': 'chicken',
        'owner': 'tiffany',
        'weight': 2,
        'eats': 'seeds',
    },
    'peso': {
        'animal type': 'dog',
        'owner': 'eric',
        'weight': 37,
        'eats': 'shoes',
    },
}

# Display information about each pet.
for pet_name, pet_info in pets.items():
    print(f"\nHere's what I know about {pet_name.title()}:")
    for key, value in pet_info.items():
        print(f"\t{key}: {value}")
