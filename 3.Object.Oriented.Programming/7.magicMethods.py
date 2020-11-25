class Book:
    def __init__(self, title, price, author):
        super().__init__()
        self.title = title
        self.price = price 
        self.author = author
        
    # Magic Methods
    
    # use __str__ to writtren the string representation
    def __str__(self):
        return f"{self.title} is written by {self.author} and costs {self.price}"
    
    # __repr__ to return the object representation, it is more of a used for debugging easier
    def __repr__(self):
        return f"title: {self.title}, author: {self.author}, cost: {self.price}"
    
    
def main():
    b1 = Book("Hit Refresh", 500, "Satya Nadella")
    print(str(b1))
    print(repr(b1))
    
if __name__ == "__main__":
    main()