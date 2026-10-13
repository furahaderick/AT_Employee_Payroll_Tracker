"""
Unit tests for employee classes and payroll calculations.
"""

from src.models.fulltime_employee import FulltimeEmployee
from src.models.contractual_employee import ContractualEmployee
from src.models.intern import Intern


class TestFulltimeEmployee:
    """Test cases for FulltimeEmployee class."""

    def test_fulltime_compensation_calculation(self):
        """Test that full-time employee compensation equals salary."""
        employee = FulltimeEmployee(
            identifier="E001", name="John Doe", salary=5000, bonus=500, tax_rate=10
        )
        assert employee.calculate_compensation() == 5000

    def test_fulltime_tax_calculation(self):
        """Test that tax is calculated correctly for full-time employee."""
        employee = FulltimeEmployee(
            identifier="E001", name="John Doe", salary=5000, bonus=500, tax_rate=10
        )
        employee.apply_tax()
        assert employee.tax_amount == 500.0  # 10% of 5000

    def test_fulltime_net_pay_calculation(self):
        """Test that net pay is calculated correctly (gross - tax)."""
        employee = FulltimeEmployee(
            identifier="E001", name="John Doe", salary=5000, bonus=500, tax_rate=10
        )
        employee.apply_tax()
        assert employee.net_pay == 4500.0  # 5000 - 500


class TestContractualEmployee:
    """Test cases for ContractualEmployee class."""

    def test_contractual_compensation_calculation(self):
        """Test that contractual employee compensation equals rate times hours."""
        employee = ContractualEmployee(
            identifier="E002", name="Jane Smith", rate=25, bonus=200, tax_rate=12
        )
        employee.hours_worked = 40
        assert employee.calculate_compensation() == 1000  # 25 * 40

    def test_contractual_tax_calculation(self):
        """Test that tax is calculated correctly for contractual employee."""
        employee = ContractualEmployee(
            identifier="E002", name="Jane Smith", rate=25, bonus=200, tax_rate=12
        )
        employee.hours_worked = 40
        employee.apply_tax()
        assert employee.tax_amount == 120.0  # 12% of 1000


class TestIntern:
    """Test cases for Intern class."""

    def test_intern_compensation_calculation(self):
        """Test that intern compensation equals stipend."""
        intern = Intern(
            identifier="I001", name="Alice Johnson", stipend=1500, bonus=100, tax_rate=5
        )
        assert intern.calculate_compensation() == 1500

    def test_intern_net_pay_calculation(self):
        """Test that net pay is calculated correctly for intern."""
        intern = Intern(
            identifier="I001", name="Alice Johnson", stipend=1500, bonus=100, tax_rate=5
        )
        intern.apply_tax()
        assert intern.net_pay == 1425.0  # 1500 - 75
