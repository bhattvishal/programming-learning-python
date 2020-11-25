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
    
    # __eq__ is used to equality comparison
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare a Book to a non-Book")        
        
        return(self.title == value.title and 
               self.author == value.author and
               self.price == value.price)
      
    # Operator overloading    
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare a Book to a non-Book")        
        
        return self.price >= value.price
    
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare a Book to a non-Book")        
    
        return self.price <= value.price
    
def main():
    b1 = Book("Hit Refresh", 500, "Satya Nadella")
    b2 = Book("Hit Refresh", 500, "Satya Nadella")
    b3 = Book("Do It Not", 1300, "Satya Nadella")
    b4 = Book("The Difficulty of Being Good", 300, "Ram Guha")


    # Check for equality
    print(b1 == b2)
    print(b1 == b3)    
    
    # Check for conditional operator
    print(b1 > b2)
    print(b1 < b3)
    
    # Sort the array
    books = [b1, b2, b3, b4]
    books.sort()
    print([book.title for book in books])
    
    
if __name__ == "__main__":
    main()