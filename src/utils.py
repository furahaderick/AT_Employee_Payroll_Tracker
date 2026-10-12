def input_positive_number(label: str) -> int:
    while True:
        try:
            number = int(input(f"Enter the {label}: "))

            if number <= 0:
                print(f"The {label} must be greater than 0.")
                continue

            return number

        except ValueError:
            print("Invalid input. Please enter a whole number.")
