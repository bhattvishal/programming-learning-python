# To automate the process of __init__ function Python introduces Data Classes in version 3.7
# the decorator @dataclass will automatically converts this to __init__

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float
        
    def getDataInfo(self):
        return f"Title: {self.title}, Author: {self.author}"
        
b1 = Book("Hit Refresh", 235, "Satya Nadella", 500.0)
print(b1)
print(b1.getDataInfo())
