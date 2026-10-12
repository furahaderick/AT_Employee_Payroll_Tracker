from src.exceptions import (
    EmployeeNotFoundException,
    InvalidOperationSelection,
)

from src.services.payroll_service import (
    create_new_employee,
    display_all_employees,
    generate_payslips,
)


def main():

    print("=== Employee Payroll Tracker ===")

    while True:
        print()
        print("Operations Menu")
        print("1. Add a new employee")
        print("2. Display all employees")
        print("3. Generate payslips")
        print("0. Exit")

        try:
            operation = int(input("Select desired operation (number): "))

            if operation not in [0, 1, 2, 3]:
                raise InvalidOperationSelection("Invalid operation selected")

        except (InvalidOperationSelection, ValueError):
            print("Please enter a valid input")
            continue

        match operation:
            case 0:
                print()
                print("Exiting Program. Bye!")
                break

            case 1:
                print()
                try:
                    create_new_employee()
                except Exception as e:
                    print(e)

            case 2:
                print()
                display_all_employees()

            case 3:
                print()
                try:
                    generate_payslips()
                except EmployeeNotFoundException as e:
                    print(e)
                except ValueError:
                    print("Please enter valid number of hours")


if __name__ == "__main__":
    main()
