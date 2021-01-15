try:
    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))
    sum_of_2_numbers = first_number + second_number
except ValueError:
    print("Input must be an integer!")
else:
    print(f"{first_number} + {second_number} = {sum_of_2_numbers}")
