# Base Company
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_details(self):
        print(f"Company: {self.name}")
        print(f"Location: {self.location}")


# Base Employee
class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

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

    def show_details(self):
        super().show_details()
        print(f"Acquired Company: {self.acquired_company}")
        print("\nEmployees:")
        for emp in self.employees:
            print("-----------------")
            emp.show_details()


# Multi-level inheritance
class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company

    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")


class Manager(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date,
                 previous_company, team_size):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.team_size = team_size

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")


class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date,
                 previous_company, policies_handled):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.policies_handled = policies_handled

    def show_details(self):
        super().show_details()
        print(f"Policies Handled: {self.policies_handled}")


class Developer(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date,
                 previous_company, programming_languages):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.programming_languages = programming_languages

    def show_details(self):
        super().show_details()
        print(f"Languages: {', '.join(self.programming_languages)}")


class Intern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation, joining_date,
                 previous_company, duration):
        super().__init__(emp_id, emp_name, designation, joining_date, previous_company)
        self.duration = duration

    def show_details(self):
        super().show_details()
        print(f"Duration: {self.duration} months")


# Multiple inheritance
class ManagerHR(Manager, HR):
    def __init__(self, emp_id, emp_name, designation, joining_date,
                 previous_company, team_size, policies_handled):
        NewEmployee.__init__(self, emp_id, emp_name, designation,
                             joining_date, previous_company)
        self.team_size = team_size
        self.policies_handled = policies_handled

    def show_details(self):
        super().show_details()
        print(f"HR Policies: {self.policies_handled}")


class DeveloperIntern(Developer, Intern):
    def __init__(self, emp_id, emp_name, designation, joining_date,
                 previous_company, programming_languages, duration):
        NewEmployee.__init__(self, emp_id, emp_name, designation,
                             joining_date, previous_company)
        self.programming_languages = programming_languages
        self.duration = duration

    def show_details(self):
        super().show_details()
        print(f"Internship Duration: {self.duration} months")



if __name__ == "__main__":

    company = CompanyAcquisition("TechNova", "Mumbai", "CodeSphere")

    emp1 = Manager(101, "Pranav", "Project Manager", "2024-01-10", "CodeSphere", 12)
    emp2 = HR(102, "Rohan", "HR Executive", "2023-11-15", "CodeSphere", 6)
    emp3 = Developer(103, "Prasad", "Software Developer", "2024-02-01",
                     "CodeSphere", ["Python", "Java"])
    emp4 = Intern(104, "Shubham", "Intern", "2024-03-01", "CodeSphere", 6)
    emp5 = ManagerHR(105, "Amit", "Senior Manager", "2023-12-01",
                     "CodeSphere", 18, 10)
    emp6 = DeveloperIntern(106, "Kunal", "Dev Intern", "2024-04-01",
                           "CodeSphere", ["Python", "C++"], 4)

    company.add_employee(emp1)
    company.add_employee(emp2)
    company.add_employee(emp3)
    company.add_employee(emp4)
    company.add_employee(emp5)
    company.add_employee(emp6)

    company.show_details()
