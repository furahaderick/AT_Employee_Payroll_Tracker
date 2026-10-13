from src.models.base_employee import Employee


class FulltimeEmployee(Employee):
    """
    Represents a full-time employee with salary-based compensation.

    Full-time employees receive a fixed salary as their gross compensation,
    regardless of hours worked. They are eligible for bonuses and subject to
    tax deductions based on their tax rate.

    Attributes:
        identifier (str): Unique identifier for the employee.
        name (str): Full name of the employee.
        salary (float): Fixed monthly or annual salary for the employee.
        bonus (float): Bonus amount for the employee.
        tax_rate (float): Tax rate percentage (1-100) for the employee.
    """

    def __init__(
        self, identifier: str, name: str, salary: float, bonus: float, tax_rate: float
    ) -> None:
        """
        Initialize a FulltimeEmployee instance.

        Args:
            identifier: Unique identifier for the employee.
            name: Full name of the employee.
            salary: Fixed salary for the employee.
            bonus: Bonus amount for the employee.
            tax_rate: Tax rate percentage (1-100) for the employee.
        """
        super().__init__(
            identifier=identifier, name=name, bonus=bonus, tax_rate=tax_rate
        )
        self.salary = salary

    @property
    def salary(self) -> float:
        """Get the salary of the full-time employee."""
        return self._salary

    @salary.setter
    def salary(self, salary: float) -> None:
        """
        Set the salary for the full-time employee.

        Args:
            salary: The salary amount to set.

        Raises:
            ValueError: If the salary is less than 0.
        """
        if salary < 0:
            raise ValueError("Employee salary cannot be less than 0")

        self._salary = salary

    def __str__(self) -> str:
        """
        Return a string representation of the full-time employee.

        Returns:
            A formatted string containing employee ID, type, name, and salary.
        """
        return (
            f"Employee ID:    {self.identifier}\n"
            "Employee Type:    Full-time\n"
            f"Employee Name:    {self.name}\n"
            f"Employee Salary:    {self.salary}"
        )

    # pylint: disable=arguments-differ
    def calculate_compensation(self) -> float:
        """
        Calculate the gross compensation for a full-time employee.

        For full-time employees, compensation is simply their fixed salary.

        Returns:
            The salary amount as gross compensation.
        """
        return self.salary

    # pylint: disable=arguments-differ
    def generate_payslip(self) -> str:
        """
        Generate a payslip for the full-time employee.

        Returns:
            A formatted payslip string containing employee details,
            gross compensation, bonus, tax, and net pay.
        """
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
