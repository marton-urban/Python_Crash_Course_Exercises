from random import choice


def check_if_won():
    for element in my_ticket.randomized:
        if element not in winning_ticket.randomized:
            my_ticket.won = False
            break
        else:
            my_ticket.won = True


class RandomSelect4:
    """Pulls 4 cards from possibilities + checks my_ticket against winning_ticket"""

    def __init__(self, won=False):
        self.randomized = []
        self.won = won

    def randomize(self):
        self.randomized = []
        while len(self.randomized) < 4:
            pulled_item = choice(possibilities)
            if pulled_item not in self.randomized:
                self.randomized.append(pulled_item)
        if self == my_ticket:
            check_if_won()


possibilities = [2, 33, 44, 7, 9, 5, 34, 56, 54, 243, 'b', 'r', 't', 'a', 'e']
my_ticket = RandomSelect4()
winning_ticket = RandomSelect4()
plays = 0

while not my_ticket.won:
    winning_ticket.randomize()
    my_ticket.randomize()
    plays += 1

print("Your ticket: ", end='')
print(*my_ticket.randomized)
print("Winning ticket: ", end='')
print(*winning_ticket.randomized)
print(f"It only took {plays} tries to win!")
