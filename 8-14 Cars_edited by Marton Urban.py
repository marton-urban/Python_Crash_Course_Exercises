def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    options['manufacturer'] = manufacturer.title()
    options['model'] = model.title()

    return options


my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white', headlights='popup')
print(my_old_accord)
