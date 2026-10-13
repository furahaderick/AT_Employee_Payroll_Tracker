from src.models.base_employee import Employee


class ContractualEmployee(Employee):
    """
    Represents a contractual employee with hourly rate-based compensation.

    Contractual employees are paid based on their hourly rate multiplied by
    the number of hours worked. They are eligible for bonuses and subject to
    tax deductions based on their tax rate.

    Attributes:
        identifier (str): Unique identifier for the employee.
        name (str): Full name of the employee.
        rate (float): Hourly rate for the employee.
        bonus (float): Bonus amount for the employee.
        tax_rate (float): Tax rate percentage (1-100) for the employee.
        hours_worked (float): Number of hours worked by the employee.
    """

    def __init__(
        self, identifier: str, name: str, rate: float, bonus: float, tax_rate: float
    ) -> None:
        """
        Initialize a ContractualEmployee instance.

        Args:
            identifier: Unique identifier for the employee.
            name: Full name of the employee.
            rate: Hourly rate for the employee.
            bonus: Bonus amount for the employee.
            tax_rate: Tax rate percentage (1-100) for the employee.
        """
        super().__init__(identifier, name, bonus, tax_rate)
        self.rate = rate

    @property
    def rate(self) -> float:
        """Get the hourly rate of the contractual employee."""
        return self._rate

    @rate.setter
    def rate(self, rate: float) -> None:
        """
        Set the hourly rate for the contractual employee.

        Args:
            rate: The hourly rate to set.

        Raises:
            ValueError: If the rate is less than 0.
        """
        if rate < 0:
            raise ValueError("Employee rate cannot be less than zero")

        self._rate = rate

    # pylint: disable=arguments-differ
    def generate_payslip(self) -> str:
        """
        Generate a payslip for the contractual employee.

        Returns:
            A formatted payslip string containing employee details,
            hours worked, gross compensation, bonus, tax, and net pay.
        """
        compensation = self.calculate_compensation()
        payslip = (
            "\n== PAYSLIP ==\n"
            f"{self}\n"
            f"Hours worked:  {self.hours_worked}\n"
            f"Gross compensation: {compensation}\n"
            f"Bonus: {self.bonus}\n"
            f"Tax: {self.tax_amount}\n"
            f"Net pay: {self.net_pay}"
        )
        return payslip

    def __str__(self) -> str:
        """
        Return a string representation of the contractual employee.

        Returns:
            A formatted string containing employee ID, type, name, and hourly rate.
        """
        return (
            f"Employee ID:    {self.identifier}\n"
            "Employee Type:    Contractual\n"
            f"Employee Name:    {self.name}\n"
            f"Employee Rate:    {self.rate}"
        )

    # pylint: disable=arguments-differ
    def calculate_compensation(self) -> float:
        """
        Calculate the gross compensation for a contractual employee.

        For contractual employees, compensation is calculated as the hourly
        rate multiplied by the number of hours worked.

        Returns:
            The calculated gross compensation (rate × hours_worked).
        """
        return self.rate * self.hours_worked
