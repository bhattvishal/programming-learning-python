# in Callable object you can actually call an object as a function to change the values

class Book:
    def __init__(self, title, price, author):
        super().__init__()
        self.title = title
        self.price = price 
        self.author = author
        
    def __str__(self):
        return f"Book {self.title} is written {self.author} and costs {self.price}"
    
    def __call__(self, title, price, author):
        self.title = title
        self.price = price 
        self.author = author
        
        
b1 = Book("Hit Refresh", 500.0, "Satya Nadella")
print(b1)

b1("Hit Again", 450.0, "Satya Nadella")
print(b1)

