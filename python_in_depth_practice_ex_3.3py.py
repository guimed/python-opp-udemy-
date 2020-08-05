class SalesPerson:
    names = []
    total_revenue = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(name)

    def make_sale(self, money):
        self.sales_amount += money
        SalesPerson.total_revenue += money

    def show_performance(self):
        print(self.name, self.age, self.sales_amount)



