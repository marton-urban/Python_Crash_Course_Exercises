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


class Admin(User):
    def __init__(self, first_name, last_name, age, country, hobby):
        super().__init__(first_name, last_name, age, country, hobby)
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.list_of_privileges = []

    def show_privileges(self):
        print(f"\nPrivileges:")
        for privilege in self.list_of_privileges:
            print(f"- {privilege}")


main_admin = Admin('márton', 'urbán', 33, 'hungary', 'programming')
main_admin.privileges.list_of_privileges = ['can add users', 'can ban users', 'can delete post']

main_admin.privileges.show_privileges()
