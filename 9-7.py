class User:
    """A simple user profile"""

    def __init__(self, first_name, last_name, age, country, hobby):
        self.hobby = hobby
        self.country = country.title()
        self.age = age
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0

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

    def increment_login_attempts(self, incrementby):
        self.login_attempts += incrementby

    def reset_login_attempts(self):
        self.login_attempts = 0


first_user = User('márton', 'urbán', 33, 'hungary', 'programming')
first_user.increment_login_attempts(2)
first_user.increment_login_attempts(3)
first_user.increment_login_attempts(4)
print(first_user.login_attempts)

first_user.reset_login_attempts()
print(first_user.login_attempts)
