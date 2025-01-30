from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_wage * self.hours_worked

# Sử dụng
ft_employee = FullTimeEmployee("John", 5000)
pt_employee = PartTimeEmployee("Alice", 20, 80)

print("Lương nhân viên full-time:", ft_employee.calculate_salary())  # ✅ 5000
print("Lương nhân viên part-time:", pt_employee.calculate_salary())  # ✅ 1600
