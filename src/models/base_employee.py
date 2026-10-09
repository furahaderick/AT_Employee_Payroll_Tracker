from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, identifier: str, name: str) -> None:
        self.identifier = identifier
        self.name = name

    @abstractmethod
    def calculate_compensation(self) -> float: ...

    @abstractmethod
    def __str__(self) -> str: ...

    @abstractmethod
    def generate_payslip(self) -> None: ...
