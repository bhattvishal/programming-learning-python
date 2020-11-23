class NewsPaper:
    def __init__(self, name):
        self.name = name

class Book:
    
    BOOK_TYPES = ("PAPERBACK", "HARDCOVER", "EBOOK")
    
    def __init__(self, title, author, pages, price, booktype):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        if (booktype not in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype
        self.__secret = 123 # this is hiding the attrbute


    __booklist = None
    
    @staticmethod
    def getBookList():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist 

    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES
    
    
    def setTitle(self, newTitle):
        self.title = newTitle
    
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price    
    
    def setDiscount(self, amount):
        self._discount = amount
 
 
 
        
print(Book.getBookTypes())        
b1 = Book("Hello New world", "Angad Bhatt", 123, 345.50, "HARDCOVER")
b1 = Book("Hello", "Angad Bhatt", 123, 345.50, "PAPERBOOK")

theBooks = Book.getBookList()
theBooks.append(b1)

  
        
# b1 = Book("Hello New world", "Angad Bhatt", 123, 345.50)
# b2 = Book("I am Angad", "Vishal Bhatt", 342, 690.75)


# n1 = NewsPaper("The Hindu")


# print(b1.getPrice())

# print(b2.getPrice())
# print(b2.setDiscount(0.25))
# print(b2.getPrice())

# print(type(b1))
# print(type(n1))

# print(isinstance(b1, Book))
# print(isinstance(n1, Book))

#print(b2.__secret) # Will give error
#print(b2._Book__secret)