class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        return f"name {self.name} age {self.age}"
    
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def show_info(self):
        return f"name {self.name} salary: {self.salary}"
    
emp = Employee("Bob", 30 , 5000)

print(emp.show_info())
print(emp.age)