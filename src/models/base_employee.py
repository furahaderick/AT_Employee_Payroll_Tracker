from abc import ABC, abstractmethod


class Employee(ABC):
    """
    Abstract base class representing an employee in the payroll system.

    This class defines the common attributes and methods shared by all employee types,
    including identifier, name, bonus, tax rate, and hours worked. It also provides
    the interface for compensation calculation and payslip generation.

    Attributes:
        identifier (str): Unique identifier for the employee.
        name (str): Full name of the employee.
        _bonus (float): Bonus amount for the employee (private property).
        _tax_rate (float): Tax rate percentage (1-100) for the employee (private property).
        hours_worked (float): Number of hours worked by the employee.
        _tax_amount (float): Calculated tax amount (private property).
    """

    def __init__(
        self, identifier: str, name: str, bonus: float, tax_rate: float
    ) -> None:
        """
        Initialize an Employee instance.

        Args:
            identifier: Unique identifier for the employee.
            name: Full name of the employee.
            bonus: Bonus amount for the employee.
            tax_rate: Tax rate percentage (1-100) for the employee.
        """
        self.identifier = identifier
        self.name = name
        self._bonus = bonus
        self._tax_rate = tax_rate
        self.hours_worked = 0.0
        self._tax_amount = 0.0

    @property
    def bonus(self) -> float:
        """Get the bonus amount for the employee."""
        return self._bonus

    @bonus.setter
    def bonus(self, bonus: float) -> None:
        """
        Set the bonus amount for the employee.

        Args:
            bonus: The bonus amount to set.

        Raises:
            ValueError: If the bonus is less than 0.
        """
        if bonus < 0:
            raise ValueError("Bonus cannot be less than 0")
        self._bonus = bonus

    @property
    def tax_rate(self) -> float:
        """Get the tax rate percentage for the employee."""
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate: float) -> None:
        """
        Set the tax rate percentage for the employee.

        Args:
            tax_rate: The tax rate percentage (1-100).

        Raises:
            ValueError: If the tax rate is not in the range (1-100).
        """
        if tax_rate <= 0 or tax_rate > 100:
            raise ValueError("Tax rate must be in the range (1 - 100)")
        self._tax_rate = tax_rate

    @property
    def tax_amount(self) -> float:
        """Get the calculated tax amount for the employee."""
        return self._tax_amount

    @property
    def net_pay(self) -> float:
        """
        Calculate and return the net pay for the employee.

        Net pay is calculated as gross compensation minus tax amount.

        Returns:
            The net pay amount.
        """
        gross = self.calculate_compensation()
        return gross - self._tax_amount

    @abstractmethod
    def calculate_compensation(self) -> float:
        """
        Calculate the gross compensation for the employee.

        This method must be implemented by subclasses to define
        type-specific compensation calculation logic.

        Returns:
            The gross compensation amount.
        """
        ...

    @abstractmethod
    def __str__(self) -> str:
        """
        Return a string representation of the employee.

        This method must be implemented by subclasses to provide
        type-specific employee information.

        Returns:
            A formatted string containing employee details.
        """
        ...

    @abstractmethod
    def generate_payslip(self) -> str:
        """
        Generate a payslip for the employee.

        This method must be implemented by subclasses to create
        type-specific payslip formatting.

        Returns:
            A formatted payslip string.
        """
        ...

    def apply_tax(self) -> None:
        """
        Calculate and apply tax to the employee's compensation.

        The tax amount is calculated as a percentage of the gross
        compensation based on the employee's tax rate.
        """
        gross = self.calculate_compensation()
        self._tax_amount = gross * (self.tax_rate / 100)
