class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies
        
        

    def display(self):
        print(' isbn: %s \n title: %s \n price: R$%s \n copies: %s .' % (self.isbn, self.title, self.price, self.copies))
        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price >= 50:
            self._price = new_price
        else:
            raise ValueError('Price must be R$50 or higher')
        
    def in_stock(self):
        if self.copies > 0:
            return True
        
    def sell(self):
        availability = self.in_stock()
        if availability:
            self.copies -= 1
        else:
            print (' %s is out of stock.' % (self.title))


book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200, 6)
        
books = [book1, book2, book3, book4]

for i in books:
    i.display()
    print()

print('Books by Jack: \n')

jacks_books = []
for k in books:
    if k.author == 'Jack':
        jacks_books.append(k)

for b in jacks_books:
    b.display()
    print()
    

