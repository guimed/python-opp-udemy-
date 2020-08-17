class Employee:
    domains = set()
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        domain = email[email.index('@') + 1 :]
        Employee.domains.add(domain)
   
    def display(self):
        print(self.name + ': ' + self.email)
