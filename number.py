three_different_numbers = input("Provide 3 different whole numbers each followed by a space: ")

# Check if the input contains exactly 3 numbers separated by spaces
if len(three_different_numbers.split()) != 3:
    print("Error: Please provide exactly three numbers separated by spaces.")
else:
    # Split the input string into a list of strings
    assign_numbers = three_different_numbers.split()

    # Check if all elements in the list are digits
    if assign_numbers[0].isdigit() and assign_numbers[1].isdigit() and assign_numbers[2].isdigit():
        # Convert the strings into integers
        a = int(assign_numbers[0])
        b = int(assign_numbers[1])
        c = int(assign_numbers[2])

        # Perform calculations
        sum_numbers = a + b + c
        first_minus_second = a - b
        third_by_first = c * a

        # Check if 'c' is zero to avoid division by zero
        if c != 0:
            sum_and_divide = sum_numbers / c
        else:
            print("Error: Division by zero is not allowed.")
            sum_and_divide = None

        # Output results
        if sum_and_divide is not None:
            print("Numbers entered:", three_different_numbers)
            print("Sum of numbers entered:", sum_numbers)
            print("The first number minus the second number:", first_minus_second)
            print("The third number times the first number:", third_by_first)
            print("The sum of numbers divided by the last number entered:", sum_and_divide)
    else:
        print("Error: Please provide valid whole numbers.")
