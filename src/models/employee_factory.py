from src.models.fulltime_employee import FulltimeEmployee
from src.models.contractual_employee import ContractualEmployee
from src.models.intern import Intern


class EmployeeFactory:

    @staticmethod
    def create_fulltime_employee(
        identifier: str, name: str, salary: float, bonus: float, tax_rate: float
    ) -> FulltimeEmployee:
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
        return ContractualEmployee(
            identifier=identifier, name=name, rate=rate, bonus=bonus, tax_rate=tax_rate
        )

    @staticmethod
    def create_intern(
        identifier: str, name: str, stipend: float, bonus: float, tax_rate: float
    ) -> Intern:
        return Intern(
            identifier=identifier,
            name=name,
            stipend=stipend,
            bonus=bonus,
            tax_rate=tax_rate,
        )
