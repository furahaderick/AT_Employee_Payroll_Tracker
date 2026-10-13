from src.models.base_employee import Employee


class Intern(Employee):

    def __init__(
        self, identifier: str, name: str, stipend: float, bonus: float, tax_rate: float
    ) -> None:
        super().__init__(identifier, name, bonus, tax_rate)
        self.stipend = stipend

    @property
    def stipend(self) -> float:
        return self._stipend

    @stipend.setter
    def stipend(self, stipend: float) -> None:
        if stipend < 0:
            raise ValueError("Intern stipend cannot be less than 0")

        self._stipend = stipend

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

    def __str__(self) -> str:
        return (
            f"Employee ID:    {self.identifier}\n"
            "Employee Type:    Intern\n"
            f"Employee Name:    {self.name}\n"
            f"Intern Stipend:    {self.stipend}"
        )

    # pylint: disable=arguments-differ
    def calculate_compensation(self) -> float:
        return self.stipend
