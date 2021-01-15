from random import choice


class RandomSelect4:
    """Pulls 4 cards from possibilities + checks my_ticket against winning_ticket"""

    def __init__(self):
        self.won = False
        self.plays = 0

    def randomize(self):
        self.randomized = []
        while len(self.randomized) < 4:
            pulled_item = choice(possibilities)
            if pulled_item not in self.randomized:
                self.randomized.append(pulled_item)

    def check_if_won(self):
        my_ticket.plays += 1
        for element in my_ticket.randomized:
            if element not in winning_ticket.randomized:
                return
        my_ticket.won = True


possibilities = [2, 33, 44, 7, 9, 5, 34, 56, 54, 243, 'b', 'r', 't', 'a', 'e']
my_ticket = RandomSelect4()
winning_ticket = RandomSelect4()

while not my_ticket.won:
    winning_ticket.randomize()
    my_ticket.randomize()
    my_ticket.check_if_won()

print("Your ticket: ", end='')
print(*my_ticket.randomized)
print("Winning ticket: ", end='')
print(*winning_ticket.randomized)
print(f"It only took {my_ticket.plays} tries to win!")
