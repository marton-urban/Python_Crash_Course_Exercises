from random import choice


class RandomSelect4:
    """Pulls 4 cards from possibilities + checks my_ticket against winning_ticket"""

    def randomize(self):
        self.randomize = []
        while len(self.randomize) < 4:
            pulled_item = choice(possibilities)
            if pulled_item not in self.randomize:
                self.randomize.append(pulled_item)

    def isnota(self, winning_ticket):
        self.winning_ticket = winning_ticket


possibilities = [2, 33, 44, 7, 9, 5, 34, 56, 54, 243, 'b', 'r', 't', 'a', 'e']
my_ticket = RandomSelect4()
winning_ticket = RandomSelect4()

plays = 0
won = False
while not won:
    my_ticket.randomize
    winning_ticket.randomize
    plays += 1