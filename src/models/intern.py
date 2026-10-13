from src.models.base_employee import Employee


class Intern(Employee):
    """
    Represents an intern with stipend-based compensation.

    Interns receive a fixed stipend as their gross compensation,
    regardless of hours worked. They are eligible for bonuses and subject to
    tax deductions based on their tax rate.

    Attributes:
        identifier (str): Unique identifier for the intern.
        name (str): Full name of the intern.
        stipend (float): Fixed stipend amount for the intern.
        bonus (float): Bonus amount for the intern.
        tax_rate (float): Tax rate percentage (1-100) for the intern.
    """

    def __init__(
        self, identifier: str, name: str, stipend: float, bonus: float, tax_rate: float
    ) -> None:
        """
        Initialize an Intern instance.

        Args:
            identifier: Unique identifier for the intern.
            name: Full name of the intern.
            stipend: Fixed stipend amount for the intern.
            bonus: Bonus amount for the intern.
            tax_rate: Tax rate percentage (1-100) for the intern.
        """
        super().__init__(identifier, name, bonus, tax_rate)
        self.stipend = stipend

    @property
    def stipend(self) -> float:
        """Get the stipend amount for the intern."""
        return self._stipend

    @stipend.setter
    def stipend(self, stipend: float) -> None:
        """
        Set the stipend amount for the intern.

        Args:
            stipend: The stipend amount to set.

        Raises:
            ValueError: If the stipend is less than 0.
        """
        if stipend < 0:
            raise ValueError("Intern stipend cannot be less than 0")

        self._stipend = stipend

    # pylint: disable=arguments-differ
    def generate_payslip(self) -> str:
        """
        Generate a payslip for the intern.

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

    def __str__(self) -> str:
        """
        Return a string representation of the intern.

        Returns:
            A formatted string containing employee ID, type, name, and stipend.
        """
        return (
            f"Employee ID:    {self.identifier}\n"
            "Employee Type:    Intern\n"
            f"Employee Name:    {self.name}\n"
            f"Intern Stipend:    {self.stipend}"
        )

    # pylint: disable=arguments-differ
    def calculate_compensation(self) -> float:
        """
        Calculate the gross compensation for an intern.

        For interns, compensation is simply their fixed stipend.

        Returns:
            The stipend amount as gross compensation.
        """
        return self.stipend
