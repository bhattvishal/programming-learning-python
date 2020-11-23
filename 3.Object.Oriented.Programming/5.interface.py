# Unlike other programming langagues like C# and Java, Python DOES NOT have in-built support
# for interface, but we can get it using multiple INHERITANCE and ABSTRACT CLASSES
# interface can also be referred as PROMISE/CONTRACT as often in Software World to provide certain
# type of Behavior and Capability

from abc import ABC, abstractmethod

# In order to make a class abstract, you must inherit from ABC class
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    # In order to mark any method abstract, you must decorate the method with @abstractmethod attribute
    @abstractmethod
    def calculateArea():
        pass
    
class JSONify(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def toJSON(self):
        pass

class Circle(GraphicShape, JSONify):    
    def __init__(self, radius):
        self.radius = radius
        
    def calculateArea(self):
        return 3.14 * (self.radius ** 2)   
    
    # just return the hardcoded json
    def toJSON(self):
        return f"{{\"area\" : {str(self.calculateArea())}}}"
    

def main():
    c = Circle(10)
    print(c.calculateArea())  
    print(c.toJSON())
    
if __name__ == "__main__":
    main()