class Employee:
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
       
    def display(self):
        print(self.name + ': ' + self.email)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        domain = new_email[new_email.index('@') + 1 :]
        if domain in Employee.allowed_domains:
            self._email = new_email
        else:
            raise RuntimeError(f'Domain {domain} not allowed')
 




        
