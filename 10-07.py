while True:
    try:
        first_number = input("First number: ")
        if first_number == 'q':
            break
        first_number = int(first_number)
        second_number = input("Second number: ")
        if second_number == 'q':
            break
        second_number = int(second_number)
        sum_of_2_numbers = first_number + second_number
    except ValueError:
        print("Input must be an integer!")
    else:
        print(f"{first_number} + {second_number} = {sum_of_2_numbers}")
