favorite_numbers = {
    'mandy': [42],
    'micah': [23, 3434],
    'gus': [7, 8, 9],
    'hank': [1000000, 27, 23, 43, 34, 34],
    'maggie': [0]
}

name = 'mandy'
print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")

name = 'micah'
print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")

name = 'gus'
print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")

name = 'hank'
print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")

name = 'maggie'
print(f"{name.title()}'s favorite number is {favorite_numbers[name]}.")

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers:", end=" ")
    for number in numbers:
        print(f"{number}", end=" ")
print()

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}")
print()

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"\n{name.title()}'s favorite number is {numbers[0]}.", end="")
    else:
        print(f"\n{name.title()}'s favorite numbers are ", end="")
        for number in numbers[:-2]:
            print(f"{number}, ", end="")
        print(f"{numbers[-2]} and {numbers[-1]}.", end="")
print()
