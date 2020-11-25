from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float
        
    def __post_init__(self):
        self.description = f"Book {self.title} is written {self.author} and costs {self.price}"   
        
b1 = Book("Hit Refresh", 235, "Satya Nadella", 500.0)
print(b1)
print(b1.description)