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


def input_percentage(label: str) -> float:
    while True:
        try:
            percentage = float(input(f"Enter the {label} percentage (1-100): "))

            if percentage < 1 or percentage > 100:
                print(f"The {label} percentage must be between 1 and 100.")
                continue

            return percentage

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
