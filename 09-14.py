from random import randint

my_list = [2, 33, 44, 7, 9, 5, 34, 56, 54, 243, 'b', 'r', 't', 'a', 'e']

print("The winning combination:")
for char in range(4):
    length_of_list = len(my_list) - 1
    print(my_list.pop(randint(0, length_of_list)))