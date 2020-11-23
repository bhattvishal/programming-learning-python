# In Composition we create complex objects from the simple objects

class Author:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
class Chapter:
    def __init__(self, name, pageCount):
        self.name = name
        self.pageCount = pageCount

class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price        
        self.author = author           
        self.chapters = []        
        
    def addChapters(self, chapter=None):
        self.chapters.append(chapter)   

    def getBookPageCount(self):
        count = 0
        for ch in self.chapters:
            count += ch.pageCount
        return count
    
def main():
    b = Book("Hit Refresh", 500, Author("Satya", "Nadella"))
    b.addChapters(Chapter("Chapter 1", 12))
    b.addChapters(Chapter("Chapter 2", 28))
    b.addChapters(Chapter("Chapter 3", 120))
    print(b.getBookPageCount())
    
    
if __name__ == "__main__":
    main()
