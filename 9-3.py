class User:
    """A simple user profile"""

    def __init__(self, first_name, last_name, age, country, hobby):
        self.hobby = hobby
        self.country = country.title()
        self.age = age
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def describe_user(self):
        print(
            f"\nFirst name: {self.first_name}"
            f"\nLast name: {self.last_name}"
            f"\nAge: {self.age}"
            f"\nCountry: {self.country}"
            f"\nHobby: {self.hobby}"
        )

    def greet_user(self):
        print(f"\nWelcome to my program, dear {self.first_name}!")


first_user = User('márton', 'urbán', 33, 'hungary', 'programming')
User.describe_user(first_user)
User.greet_user(first_user)