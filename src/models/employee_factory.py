from src.models.fulltime_employee import FulltimeEmployee
from src.models.contractual_employee import ContractualEmployee
from src.models.intern import Intern


class EmployeeFactory:
    """
    Factory class for creating employee instances.

    This factory centralizes the creation logic for different employee types,
    providing a clean interface for instantiating FulltimeEmployee,
    ContractualEmployee, and Intern objects.
    """

    @staticmethod
    def create_fulltime_employee(
        identifier: str, name: str, salary: float, bonus: float, tax_rate: float
    ) -> FulltimeEmployee:
        """
        Create a full-time employee instance.

        Args:
            identifier: Unique identifier for the employee.
            name: Full name of the employee.
            salary: Fixed salary for the employee.
            bonus: Bonus amount for the employee.
            tax_rate: Tax rate percentage (1-100) for the employee.

        Returns:
            A FulltimeEmployee instance with the specified attributes.
        """
        return FulltimeEmployee(
            identifier=identifier,
            name=name,
            salary=salary,
            bonus=bonus,
            tax_rate=tax_rate,
        )

    @staticmethod
    def create_contractual_employee(
        identifier: str, name: str, rate: float, bonus: float, tax_rate: float
    ) -> ContractualEmployee:
        """
        Create a contractual employee instance.

        Args:
            identifier: Unique identifier for the employee.
            name: Full name of the employee.
            rate: Hourly rate for the employee.
            bonus: Bonus amount for the employee.
            tax_rate: Tax rate percentage (1-100) for the employee.

        Returns:
            A ContractualEmployee instance with the specified attributes.
        """
        return ContractualEmployee(
            identifier=identifier, name=name, rate=rate, bonus=bonus, tax_rate=tax_rate
        )

    @staticmethod
    def create_intern(
        identifier: str, name: str, stipend: float, bonus: float, tax_rate: float
    ) -> Intern:
        """
        Create an intern instance.

        Args:
            identifier: Unique identifier for the intern.
            name: Full name of the intern.
            stipend: Fixed stipend amount for the intern.
            bonus: Bonus amount for the intern.
            tax_rate: Tax rate percentage (1-100) for the intern.

        Returns:
            An Intern instance with the specified attributes.
        """
        return Intern(
            identifier=identifier,
            name=name,
            stipend=stipend,
            bonus=bonus,
            tax_rate=tax_rate,
        )
