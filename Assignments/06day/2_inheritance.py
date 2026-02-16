# Base Company
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def _financial_report(self):   # hidden method
        return "Confidential Financial Report Data"

    def show_details(self):
        print(f"Company: {self.name}")
        print(f"Location: {self.location}")


# Base Employee
class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def _policy_update(self):   # hidden method
        return "Company policy updated successfully"

    def show_details(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Designation: {self.designation}")


# Company Acquisition
class CompanyAcquisition(Company):
    def __init__(self, name, location, acquired_company):
        super().__init__(name, location)
        self.acquired_company = acquired_company
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_details(self):   # overridden
        super().show_details()
        print(f"Acquired Company: {self.acquired_company}")
        print("\nEmployees:")
        for emp in self.employees:
            print("----------------")
            emp.show_details()


# Multi-level inheritance
class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company

    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")


# Manager (can access financial report)
class Manager(NewEmployee):
    def access_financials(self, company):
        print("Manager Accessing Financial Report:")
        print(company._financial_report())

    def show_details(self):
        super().show_details()
        print("Role: Manager")


# HR (can access policy update)
class HR(NewEmployee):
    def update_policy(self):
        print("HR Updating Policy:")
        print(self._policy_update())

    def show_details(self):
        super().show_details()
        print("Role: HR")


# Developer (restricted)
class Developer(NewEmployee):
    def show_details(self):
        super().show_details()
        print("Role: Developer")


# Intern (restricted)
class Intern(NewEmployee):
    def show_details(self):
        super().show_details()
        print("Role: Intern")


# Multiple + Hybrid inheritance
class ManagerHR(Manager, HR):
    def show_details(self):
        super().show_details()
        print("Role: Manager + HR")


class DeveloperIntern(Developer, Intern):
    def show_details(self):
        super().show_details()
        print("Role: Developer + Intern")



if __name__ == "__main__":

    company = CompanyAcquisition("TechNova", "Pune", "CodeSphere")

    emp1 = Manager(101, "Pranav", "Project Manager",
                   "2024-01-10", "CodeSphere")

    emp2 = HR(102, "Rohan", "HR Executive",
              "2023-11-15", "CodeSphere")

    emp3 = Developer(103, "Prasad", "Software Developer",
                     "2024-02-01", "CodeSphere")

    emp4 = Intern(104, "Shubham", "Intern",
                  "2024-03-01", "CodeSphere")

    emp5 = ManagerHR(105, "Amit", "Senior Manager",
                     "2023-12-01", "CodeSphere")

    emp6 = DeveloperIntern(106, "Kunal", "Dev Intern",
                           "2024-04-01", "CodeSphere")

    company.add_employee(emp1)
    company.add_employee(emp2)
    company.add_employee(emp3)
    company.add_employee(emp4)
    company.add_employee(emp5)
    company.add_employee(emp6)

    company.show_details()

    print("\n--- Restricted Access Demo ---")
    emp1.access_financials(company)   # Allowed
    emp2.update_policy()              # Allowed

    emp3._policy_update()  #  Not allowed logically
    # emp3._financial_report()  Not allowed logically
