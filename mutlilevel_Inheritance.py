class Emp:
    def __init__(self, id, emp_name):
        self.id = id
        self.name = emp_name

    def display(self):
        print("----------Emp Details----------")
        print(f"Employee Id: {self.id} \nEmployee Name: {self.name}")


class Manager(Emp):
    def __init__(self, id, emp_name, depart):
        super().__init__(id, emp_name)
        self.depart = depart

    def display2(self, company_name):
        found = False
        for company in depart:
            if company_name in company:
                for item in company[company_name]:
                    if item["depart"].lower() == self.depart.lower():
                        found = True
                        print(f"Department: {item['depart']} \nManager Name: {item['mname']}")
        if not found:
            print(f"Sales department is not found in {company_name}")


class Director(Manager):
    def __init__(self, id, emp_name, depart, comp):
        super().__init__(id, emp_name, depart)
        self.comp = comp

    def display3(self):
        found = False
        for company in depart:
            if self.comp in company:
                for item in company[self.comp]:
                    if item["depart"].lower() == self.depart.lower():
                        found = True
                        print(f"Company: {self.comp}")
        if not found:
            print(f"{self.comp} is not available")


depart = [
    {"tcs": [
            {"depart": "sales", "mname": "Mr. Rohan Verma"},
            {"depart": "manufacture", "mname": "Ms. Riya "},
            {"depart": "hr", "mname": "Ms. Raman"}],
        "infosys": [
            {"depart": "sales", "mname": "Mr. Satish"},
            {"depart": "manufacture", "mname": "Ms. Geeta "},
            {"depart": "hr", "mname": "Ms. Manpreet"}],
        "accenture": [
            {"depart": "sales", "mname": "Ms. Meena"},
            {"depart": "manufacture", "mname": "Mr. Akshay "},
            {"depart": "hr", "mname": "Ms. Diya"}]
    }]

print("Companies and Departments:")
for company in depart:
    for company_name, departments in company.items():
        print(f"---------{company_name}---------")
        for item in departments:
            print(f"- {item['depart']} : {item['mname']}")
        print()

print("---------------------------------")
emp_id = int(input("Employee Id: "))
emp_name = input("Employee Name: ")
department = input("Department: ")
company = input("Company: ")

details = Director(emp_id, emp_name, department, company.lower())
details.display()
details.display2(company.lower())
details.display3()