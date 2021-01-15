import json


def check_fav_number():
    try:
        with open('files/fav_num.json') as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_num


def print_fav_number():
    print(f"I know your favorite number! It's {fav_num}.")


def ask_fav_number():
    fav_num = int(input("What is your favorite number? "))
    return fav_num


def save_fav_number():
    with open('files/fav_num.json', 'w') as f:
        json.dump(fav_num, f)
    print("Your favorite number has been saved for next time.")


fav_num = check_fav_number()

if fav_num:
    print_fav_number()
else:
    fav_num = ask_fav_number()
    save_fav_number()
