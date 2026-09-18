class Employee:
    company_name = "TechCorp"    # Class Variable

    def __init__(self, emp_id):
        self.emp_id = emp_id   # Instance Variable

    def calculate_salary(self):
        base_salary = 50000    # Local variable
        print(f"Company: {Employee.company_name} | ID: {self.emp_id} | Salary: {base_salary}")

emp1 = Employee(101)
emp2 = Employee(102)

emp1.calculate_salary()
emp2.calculate_salary()

