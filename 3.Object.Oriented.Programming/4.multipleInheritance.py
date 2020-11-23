# Unlike other programming languages Python DOES support MULTIPLE INHERITANCE
# But multiple inheritance are not very much used in Real World Projects

class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Tom"
        
class B: 
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Jerry"

# Class C inherits from both, class A and class B, you might have noticed that both the class have
# the same property named 'name', but this only prints the name from class A, because python gets
# in the order classes are inherited. In our case since class A is inherited first, it will print from A       
class C(A, B):
    def __init__(self):
        super().__init__()
        
    def showProperties(self):
        print(self.foo)
        print(self.bar)
        print(self.name)
        
def main():
    c = C()
    c.showProperties()
    
if __name__ == "__main__":
    main()