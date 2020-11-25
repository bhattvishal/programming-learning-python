# Sometimes we may want to create a class whose attribute can not be changed

from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutableClass:    
    pages: int    
    title: str = "No Title"
    author: str = "No Author"
    
    def someFunc(self, newValue):
        self.pages = newValue
    
b1 = ImmutableClass(100)
print(b1)

#b1.pages = 200

# You can change this even from methods in immutable classes
b1.someFunc(300)