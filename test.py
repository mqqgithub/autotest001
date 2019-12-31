class Employee:
    "dco__doc"
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count +=1

    def display_count(self):
        print("Total Employee %d" % Employee.emp_count)

    def display_employee(self):
        self.age = 12
        print(self.age)
        print("name:  ", self.name)
        print("salary:  ", self.salary)
        print(self, self.__class__)


emp1 = Employee('jack', 10000)
emp1.display_employee()

from selenium.webdriver.common.action_chains import ActionChains