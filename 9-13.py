from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides
        print(f"\nYour rolls with the {self.sides} sided die:")

    def roll_die(self):
        print(f"You rolled a {randint(1,self.sides)}.")


my_die = Die()
for roll in range(10):
    my_die.roll_die()

my_bigger_die = Die(10)
for roll in range(10):
    my_bigger_die.roll_die()

my_even_bigger_die = Die(20)
for roll in range(10):
    my_even_bigger_die.roll_die()