""".Create an abstract class LibraryItem with abstract methods borrow() and return_item(). 
Then create two subclasses:

Book, with attributes title, author, and num_copies.
DVD, with attributes title, director, and duration.
Implement a function borrow_item(item) that borrows the library item and decreases the number of available copies
 (for books) or marks the DVD as borrowed.
"""
from abc import ABC, abstractmethod
class LibraryItem(ABC):
    @abstractmethod
    def borrow(self):
        pass
    def return_item(self):
        pass
class Book(LibraryItem):
    def __init__ (self,title,author,num_copies):
        self.title=title
        self.author=author
        self.num_copies=num_copies
       
    def borrow(self):
        if self.num_copies>0:
            self.num_copies -=1
            print(f"Borrowed '{self.title}. Copies left: {self.num_copies}")
        else:
            print(f"'{self.title}' is not  available for borrowing....")
    def return_item(self):
        self.num_copies += 1
        print(f"Returned '{self.title}'.Copies available: {self.num_copies}")
class DVD(LibraryItem):
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duraction=duration
        self.is_borrowed=False
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed=True
            print(f"Borrowed DVD '{self.title}' directed by {self.director}")
        else:
            print(f"DVD '{self.title}' is already borrowed.")
    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed =False
            print(f"Returned DVD '{self.title}'.")
        else:
            print(f"DVD '{self.title}' was not borrowed.") 
def borrow_item(item):
    item.borrow()
book1=Book("2024","Devara",5 )
dvd1=DVD("Ijvhf","ngkkjkjvkj",143)
borrow_item(book1)
borrow_item(dvd1)