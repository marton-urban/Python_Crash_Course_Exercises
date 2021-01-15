user_name = input("What's your name? ")

with open('files/guest.txt', 'w') as my_file:
    my_file.write(user_name)