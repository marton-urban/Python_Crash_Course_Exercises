# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pets = [{
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
},
    {
        'animal type': 'chicken',
        'name': 'clarence',
        'owner': 'tiffany',
        'weight': 2,
        'eats': 'seeds',
    },
    {
        'animal type': 'dog',
        'name': 'peso',
        'owner': 'eric',
        'weight': 37,
        'eats': 'shoes',
    }, ]

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    del pet['name']
    for key, value in pet.items():
        print(f"\t{key}: {value}")
