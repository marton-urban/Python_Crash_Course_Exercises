class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname.title()
        self.lname = lname.title()
        self.salary = salary

    def give_raise(self, add_to_salary=5000):
        try:
            self.salary += add_to_salary
        except TypeError:
            print("Input must be an integer.")
        else:
            print("Your new salary is " + str(self.salary))


