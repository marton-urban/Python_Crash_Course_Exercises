def city_country(city_name, country_name, population=''):
    if population:
        return f"{city_name.title()}, {country_name.title()} - population {population}"
    else:
        return f"{city_name.title()}, {country_name.title()}"
