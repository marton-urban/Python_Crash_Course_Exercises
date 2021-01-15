user_name = ""
while user_name != 'q':
    user_name = input("What's your name? ")
    if user_name != 'q':
        print(f"Welcome {user_name}\n")
        with open('files/guest_book.txt', 'a') as my_file:
            my_file.write(f"{user_name}\n")
