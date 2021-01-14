class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Updates the number of served customers of given restaurant"""
        self.number_served = number_served

    def increment_number_served(self, incrementby):
        self.number_served += incrementby


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='fagyizó'):
        super().__init__(name, cuisine_type)

    def display_flavors(self):
        print("\nThe following flavors are available:")
        for flavor in self.flavors:
            print(f"\t- {flavor}")


restaurant = Restaurant('the mean queen', 'pizza')

icecream_place = IceCreamStand('sarki fagyizó')
icecream_place.flavors = ['chocolate', 'lemon', 'strawbery', 'nutella']

icecream_place.display_flavors()
