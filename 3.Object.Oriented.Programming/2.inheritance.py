# Super Class
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price
 
# Sub Super Class        
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher        
 
# Book class inherits from Publication class   
class Book(Publication):
    def __init__(self, title, price, pages, author):
        super().__init__(title, price)
        self.pages = pages
        self.author = author

# Magazine class inherits from Periodical class        
class Magazine(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)      

# NewsPaper class inherits from Periodical class     
class NewsPaper(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)       
        
        
def main():
    b1 = Book("Hit Refresh", 500, 280, "Satya Nadella")
    m1 = Magazine("Manorama", 145, "Monthly", "Penguin")
    n1 = NewsPaper("Dainik Bhaskar", 6, "Daily", "Agarwal Group")
    
    print(b1.title)
    print(n1.title)
    print(b1.price, m1.price, n1.price)
    
    
if __name__ == "__main__":
    main()