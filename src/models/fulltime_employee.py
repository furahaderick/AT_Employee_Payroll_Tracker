from src.models.base_employee import Employee


class FulltimeEmployee(Employee):

    def __init__(self, identifier: str, name: str, salary: float) -> None:
        super().__init__(identifier=identifier, name=name)
        self.salary = salary

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, salary: float) -> None:
        if salary < 0:
            raise ValueError("Employee salary cannot be less than 0")

        self._salary = salary

    def __str__(self) -> str:
        return (
            f"Employee ID:    {self.identifier}\n"
            "Employee Type:    Full-time\n"
            f"Employee Name:    {self.name}\n"
            f"Employee Salary:    {self.salary}"
        )

    # pylint: disable=arguments-differ
    def calculate_compensation(self) -> float:
        return self.salary

    # pylint: disable=arguments-differ
    def generate_payslip(self) -> None:
        compensation = self.salary
        print("\n== PAYSLIP ==")
        print(self)
        print(f"Gross compensation: {compensation}")
