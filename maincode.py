class Employee:
    """
    Holds employee's name,age and salary
    """

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Employee {self.name} has age {self.age} and salary {self.salary}.'

    def __repr__(self):
        return f'Employee(name = {self.name}, age = {self.age}, salary = {self.salary})'


class EmployeesManager:
    """
    Holds a list of employees and has implementation for the menu options (i.e, all of the function in the menu option
    can be implemented here)
    """

    def __init__(self):
        self.employees = []

    def add_employee(self):
        print("\nEnter employee data")
        name = input("Enter the name: ", )
        age = int(input("Enter the age: ", ))
        salary = int(input("Enter the salary: ", ))
        self.employees.append(Employee(name, age, salary))
        print("Employee", name, "added successfully.")

    def employee_list(self):
        print("**Employees list**")
        for members in self.employees:
            print(f"Employee: {members.name} has age {members.age} and salary {members.salary}")
        print()

    def delete_employee_by_age(self, age_from, age_to):
        if age_from > age_to:
            age_from, age_to = age_to, age_from
        for emp in self.employees:
            if age_from <= int(emp.age) <= age_to:
                print("Deleting...", emp.name)
                self.employees.remove(emp)
                print(emp.name, " deleted successfully!")

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
            return None

    def update_salary_by_name(self, name, salary):
        employee = self.find_employee_by_name(name)
        if employee is None:
            print("Error: No employee with such name")
        else:
            employee.salary = salary
            print(f"Salary of {employee.name} updated to --", salary)


class FrontEndManager:
    """
    Print the menu , get a choice and call the Employees Manager
    """

    def __init__(self):
        self.option = None
        self.employee_manager = EmployeesManager()

    def program_options(self):
        print("Program Options :\n "
              "1) Add a new employee \n "
              "2) List all employees \n "
              "3) Delete by age range \n "
              "4) Update salary given a name \n "
              "5) End the program\n ")

    def get_option(self):
        while True:
            self.option = input("Enter your choice (from 1 to 5): ", )
            if self.option not in ['1', '2', '3', '4', '5']:
                print("Invalid range. Try again!")
            else:
                break

    def run(self):
        while True:
            self.program_options()
            self.get_option()
            if self.option == '1':
                self.employee_manager.add_employee()
            elif self.option == '2':
                self.employee_manager.employee_list()
            elif self.option == '3':
                age_from = int(input("Enter age from: ", ))
                age_to = int(input("Enter age to: ", ))
                self.employee_manager.delete_employee_by_age(age_from, age_to)
            elif self.option == '4':
                name = input("Enter name: ", )
                salary = int(input("Enter salary: ", ))
                self.employee_manager.update_salary_by_name(name, salary)
            else:
                break

if __name__ == "__main__":
    app = FrontEndManager()
    app.run()





