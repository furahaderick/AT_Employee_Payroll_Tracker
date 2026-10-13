from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(
        self, identifier: str, name: str, bonus: float, tax_rate: float
    ) -> None:
        self.identifier = identifier
        self.name = name
        self._bonus = bonus
        self._tax_rate = tax_rate
        self.hours_worked = 0.0
        self._tax_amount = 0.0

    @property
    def bonus(self) -> float:
        return self._bonus

    @bonus.setter
    def bonus(self, bonus: float) -> None:
        if bonus < 0:
            raise ValueError("Bonus cannot be less than 0")
        self._bonus = bonus

    @property
    def tax_rate(self) -> float:
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate: float) -> None:
        if tax_rate <= 0 or tax_rate > 100:
            raise ValueError("Tax rate must be in the range (1 - 100)")
        self._tax_rate = tax_rate

    @property
    def tax_amount(self) -> float:
        return self._tax_amount

    @property
    def net_pay(self) -> float:
        gross = self.calculate_compensation()
        return gross - self._tax_amount

    @abstractmethod
    def calculate_compensation(self) -> float: ...

    @abstractmethod
    def __str__(self) -> str: ...

    @abstractmethod
    def generate_payslip(self) -> str: ...

    def apply_tax(self) -> None:
        gross = self.calculate_compensation()
        self._tax_amount = gross * (self.tax_rate / 100)
