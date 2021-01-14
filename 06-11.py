cities = {
    'Budapest': {
        'country': 'Hungary',
        'population': '10 000 000',
        'fact': 'kurva jó itt',
    },
    'vÁc': {
        'country': 'Hungary',
        'population': '40 000',
        'fact': 'kedvenc városom ám ez',
    },
}
for city, infos in cities.items():
    print(f"{city.title()}")
    for key, value in infos.items():
        print(f"\t{key.title()}: {value.title()}")
