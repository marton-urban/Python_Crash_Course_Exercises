filename = 'cats.txt'
try:
    with open("files/" + filename, encoding='utf-8') as f:
        cats = (f.read())
except FileNotFoundError:
    print(f"Sorry, file '{filename}' not found.")
else:
    print(cats.rstrip())

filename = 'dogs.txt'
try:
    with open('files/' + filename, encoding='utf-8') as f:
        dogs = (f.read())
except FileNotFoundError:
    print(f"Sorry, file '{filename}' not found.")
else:
    print(f"\n{dogs.rstrip()}")
