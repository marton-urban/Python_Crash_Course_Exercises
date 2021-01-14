from random import randint

my_ticket = [33, 't', 7, 'a']
counter = 0
highest = 0

while counter < 200000:
    if counter > highest:
        highest = counter
        print(highest)
    winning_ticket = []
    counter = 0
    while winning_ticket != my_ticket:
        my_list = [2, 33, 44, 7, 9, 5, 34, 56, 54, 243, 'b', 'r', 't', 'a', 'e']
        winning_ticket = []
        counter += 1
        for char in range(4):
            length_of_list = len(my_list) - 1
            winning_ticket.append(my_list.pop(randint(0, length_of_list)))

print("Your ticket: ", end="")
print(*my_ticket)
print("The winning combination: ", end="")
print(*winning_ticket)
print(f"\n It took {counter} tries to win with your ticket.")
