from src.models.contractual_employee import ContractualEmployee
from src.models.fulltime_employee import FulltimeEmployee
from src.models.intern import Intern
from src.exceptions import (
    EmployeeAlreadyExistsException,
    InvalidEmployeeTypeException,
    EmployeeNotFoundException,
)
from src.models.base_employee import Employee
from src.models.employee_factory import EmployeeFactory
from src.utils import input_positive_number


employees: list[Employee] = []


def get_employee_by_id(identifier: str) -> Employee | None:
    employee = next((e for e in employees if e.identifier == identifier), None)
    return employee


def create_new_employee():
    employee_type = input("Enter employee type (fulltime, contractual, intern): ")

    if employee_type not in ["fulltime", "contractual", "intern"]:
        raise InvalidEmployeeTypeException(f"Unknown employee type '{employee_type}'")

    identifier = input("Enter employee ID: ")

    existing_employee = get_employee_by_id(identifier=identifier)

    if existing_employee is not None:
        raise EmployeeAlreadyExistsException(
            f"Employee with ID {identifier} already exists"
        )

    name = input("Enter employee name: ")

    match employee_type:
        case "fulltime":
            salary = float(input("Enter his/her salary: "))
            new_employee = EmployeeFactory.create_fulltime_employee(
                identifier=identifier, name=name, salary=salary
            )

        case "contractual":
            rate = float(input("Enter his/her rate: "))
            new_employee = EmployeeFactory.create_contractual_employee(
                identifier=identifier, name=name, rate=rate
            )

        case "intern":
            stipend = float(input("Enter his/her stipend: "))
            new_employee = EmployeeFactory.create_intern(
                identifier=identifier, name=name, stipend=stipend
            )

    employees.append(new_employee)

    print()
    print("Employee added successfully!")
    print(f"Employee Name: {new_employee.name}")
    print(f"Employee ID: {new_employee.identifier}")


def display_all_employees():
    print("All employees")
    print()

    for e in employees:
        print("-" * 40)
        print(e)


def generate_payslips():
    identifier = input("Enter employee ID: ")

    employee = get_employee_by_id(identifier=identifier)

    if employee is None:
        raise EmployeeNotFoundException(f"Employee with ID {identifier} not found")

    if isinstance(employee, ContractualEmployee):
        hours_worked = input_positive_number("total number of hours")
        employee.generate_payslip(hours_worked=hours_worked)

    elif isinstance(employee, FulltimeEmployee):
        employee.generate_payslip()

    elif isinstance(employee, Intern):
        employee.generate_payslip()

    return
