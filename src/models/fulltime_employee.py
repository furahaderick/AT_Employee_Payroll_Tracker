from src.models.base_employee import Employee


class FulltimeEmployee(Employee):

    def __init__(
        self, identifier: str, name: str, salary: float, bonus: float, tax_rate: float
    ) -> None:
        super().__init__(
            identifier=identifier, name=name, bonus=bonus, tax_rate=tax_rate
        )
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
    def generate_payslip(self) -> str:
        compensation = self.calculate_compensation()
        payslip = (
            "\n== PAYSLIP ==\n"
            f"{self}\n"
            f"Gross compensation: {compensation}\n"
            f"Bonus: {self.bonus}\n"
            f"Tax: {self.tax_amount}\n"
            f"Net pay: {self.net_pay}"
        )
        return payslip
