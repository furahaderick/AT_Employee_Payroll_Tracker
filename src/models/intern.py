from src.models.base_employee import Employee


class Intern(Employee):

    def __init__(self, identifier: str, name: str, stipend: float) -> None:
        super().__init__(identifier, name)
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
    def generate_payslip(self) -> None:
        compensation = self.stipend
        print("\n== PAYSLIP ==")
        print(self)
        print(f"Gross compensation: {compensation}")

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
