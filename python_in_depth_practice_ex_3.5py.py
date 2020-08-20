class Employee:
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        domain = email[email.index('@') + 1 :]
        if domain not in Employee.allowed_domains:
            raise ValueError('Domain not allowed')

    def display(self):
        print(self.name + ': ' + self.email)
