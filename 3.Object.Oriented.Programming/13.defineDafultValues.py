# KEEP IN MIND: Attributes with no Default Values must come first


from dataclasses import dataclass, field
import random

def getDiscount():
    return float(random.randrange(20, 40))

@dataclass
class Book:    
    pages: int    
    title: str = "No Title"
    author: str = "No Author"
    price: float = field(default=10.0) # We can also use field to define default value
    discount: float = field(default_factory=getDiscount) # We can get the dafule from funcation
    
    
    def __post_init__(self):
        self.description = f"Book {self.title} is written {self.author} and costs {self.price}"   
        
b1 = Book(235)
print(b1)
print(b1.description)
print(b1.discount)