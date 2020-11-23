# To use Abstract methods you must import the general, ABC stands fro Abstract Base Class
from abc import ABC, abstractmethod

# In order to make a class abstract, you must inherit from ABC class
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    # In order to mark any method abstract, you must decorate the method with @abstractmethod attribute
    @abstractmethod
    def calculateArea():
        pass
    
class Circle(GraphicShape):    
    def __init__(self, radius):
        self.radius = radius
        
    def calculateArea(self):
        return 3.14 * (self.radius ** 2)   
    

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
        
    def calculateArea(self):
        return self.side * self.side        
    
def main():
    c = Circle(10)
    print(c.calculateArea())
    
    s = Square(10)
    print(s.calculateArea())
    
if __name__ == "__main__":
    main()