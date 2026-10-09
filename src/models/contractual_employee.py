from src.models.base_employee import Employee


class ContractualEmployee(Employee):

    def __init__(self, identifier: str, name: str, rate: float) -> None:
        super().__init__(identifier, name)
        self.rate = rate

    @property
    def rate(self) -> float:
        return self._rate

    @rate.setter
    def rate(self, rate: float) -> None:
        if rate < 0:
            raise ValueError("Employee rate cannot be less than zero")

        self._rate = rate

    # pylint: disable=arguments-differ
    def generate_payslip(self, hours_worked) -> None:
        compensation = self.rate * hours_worked
        print("\n== PAYSLIP ==")
        print(self)
        print(f"Hours worked:  {hours_worked}")
        print(f"Gross compensation: {compensation}")

    def __str__(self) -> str:
        return (
            f"Employee ID:    {self.identifier}\n"
            "Employee Type:    Contractual\n"
            f"Employee Name:    {self.name}\n"
            f"Employee Rate:    {self.rate}"
        )

    # pylint: disable=arguments-differ
    def calculate_compensation(self, hours_worked: float) -> float:
        return self.rate * hours_worked
