class Book:
    def __init__(self, title, price, author):
        super().__init__()
        self.title = title
        self.price = price
        self.author = author
        self._discount = 0.1
    
    def setPrice(self, newPrice):
        self.price = newPrice
        
        
    def __str__(self):
        return f"{self.title} is written by {self.author} and costs {self.price}"        
        
    def __getattribute__(self, name: str):
        if name == "price":
            # We should call the super's __getattribute__ ,else it will end calling it's own property recursively
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
            
        return super().__getattribute__(name)
    
    # This is called every time a value for a variable is set
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price must be in floats")
        return super().__setattr__(name, value)
    
    # # __getattr__ is called when __getattribute__ is not available or the property does not exits
    # def __getattr__(self, name):
    #     return name + " is not here!"
        
def main():
    b1 = Book("Hit Refresh", 500.0, "Satya Nadella")
    b2 = Book("Thinking Fast and Slow", 345.0, "Daniel Kanheman")
    
    b1.price = 400.0
    print(b1)    
    
if __name__ == "__main__":
    main()
