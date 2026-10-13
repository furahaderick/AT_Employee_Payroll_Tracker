from src.models.base_employee import Employee


class ContractualEmployee(Employee):

    def __init__(
        self, identifier: str, name: str, rate: float, bonus: float, tax_rate: float
    ) -> None:
        super().__init__(identifier, name, bonus, tax_rate)
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
    def generate_payslip(self) -> str:
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
        return (
            f"Employee ID:    {self.identifier}\n"
            "Employee Type:    Contractual\n"
            f"Employee Name:    {self.name}\n"
            f"Employee Rate:    {self.rate}"
        )

    # pylint: disable=arguments-differ
    def calculate_compensation(self) -> float:
        return self.rate * self.hours_worked
