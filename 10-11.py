import json


def json_dump(filename):
    fav_num = int(input("What is your favorite number? "))
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
    print("Your favorite number has been saved for next time.")


def json_load(filename):
    try:
        with open(filename) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        print(f"I'm sorry, I can't find '{filename}'.")
    else:
        print(f"I know your favorite number! It's {fav_num}.")


filename = 'files/fav_num.txt'
action = input("Dump or load? ").lower()

if action == 'dump':
    json_dump(filename)
elif action == 'load':
    json_load(filename)
else:
    print("Next time please don't be stupid!")
