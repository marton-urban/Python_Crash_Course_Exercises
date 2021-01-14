from random import choice, randint

my_list = [2, 33, 44, 56, 7, 5, 34, 56, 54, 7, 'b', 'r', 't', 'a', 'e']

print(
    f"The winning combination:"
    f"{my_list.pop(randint(0, 14))},"
    f"{my_list.pop(randint(0, 13))},"
    f"{my_list.pop(randint(0, 12))},"
    f"{my_list.pop(randint(0, 11))}"
)
