from src.models.fulltime_employee import FulltimeEmployee
from src.models.contractual_employee import ContractualEmployee
from src.models.intern import Intern


class EmployeeFactory:

    @staticmethod
    def create_fulltime_employee(
        identifier: str, name: str, salary: float
    ) -> FulltimeEmployee:
        return FulltimeEmployee(identifier=identifier, name=name, salary=salary)

    @staticmethod
    def create_contractual_employee(
        identifier: str, name: str, rate: float
    ) -> ContractualEmployee:
        return ContractualEmployee(identifier=identifier, name=name, rate=rate)

    @staticmethod
    def create_intern(identifier: str, name: str, stipend: float) -> Intern:
        return Intern(identifier=identifier, name=name, stipend=stipend)
