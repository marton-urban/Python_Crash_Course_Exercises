from random import randint

my_ticket = (33, 't', 7, 'a')
counter = 0
highest = 0

while counter < 260000:
    if counter > highest:
        highest = counter
        print(highest)
    counter = 0
    right_counter = 0
    while right_counter != 4:
        my_list = [2, 33, 44, 7, 9, 5, 34, 56, 54, 243, 'b', 'r', 't', 'a', 'e']
        winning_ticket = []
        counter += 1
        right_counter = 0
        for char in range(4):
            length_of_list = len(my_list) - 1
            current = my_list.pop(randint(0, length_of_list))
            if current not in my_ticket:
                break
            else:
                winning_ticket.append(current)
                right_counter += 1

print("Your ticket: ", end="")
print(*my_ticket)
print("The winning combination: ", end="")
print(*winning_ticket)
print(f"\n It took {counter} tries to win with your ticket.")
