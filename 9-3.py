class User:
    """A simple user profile"""

    def __init__(self, first_name, last_name, age, country, hobby):
        self.hobby = hobby
        self.country = country
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(
            f"\nFirst name: {self.first_name}"
            f"\nLast name: {self.last_name}"
            f"\nAge: {self.age}"
            f"\nCountry: {self.country}"
            f"\nHobby: {self.hobby}"
        )

first_user = User('Márton', 'Urbán', 33, 'Hungary', 'Programming')
User.describe_user(first_user)