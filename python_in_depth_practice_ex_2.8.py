class Product():
    def __init__(self, idt, marked_price, discount):
        self.idt = idt
        self.marked_price = marked_price
        self._discount = discount

    @property
    def selling_price(self):
        if self.marked_price > 500:
            self._discount = self._discount + 2
        
        return self.marked_price - (self.marked_price / 100) * self._discount

    

 
            

    def display(self):
        print(self.idt, self.marked_price, self._discount)

        
    
        
