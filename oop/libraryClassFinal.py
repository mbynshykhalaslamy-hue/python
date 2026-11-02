import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox




class book:
    def __init__(self,name, outhor, langauge, pages, status,price,topic):
        self.name=name
        self.outhor=outhor
        self.language=langauge
        self.pages=pages
        self.status=status
        self.price=price
        self.topic=topic

    def __str__(self):
        return(
            f"The book name: {self.name}\n"
            f"The book outhor: {self.outhor}\n"
            f"The book main Language:  {self.language}\n"
            f"The book pages:  {self.pages}\n"
            f"The Book status is: {self.status}"
        )




# print(book1)

class library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)

    def show_book(self):
        for book in self.books:
            print(book)
  

lib1=library()

book1=book('book11','mohammad','rt', 'm1', 'mmm' ,'15' , '0') 

book2=book('book12','mobin','rty', 'm1y', 'mmmy' ,'150' , '1')

book3=book('book13','ahsan','rtyn', 'm1yn', 'mmmyn' ,'123' , '0')

lib1.add_book(book1)

lib1.add_book(book2)

lib1.add_book(book3)

lib1.show_book()

# lib1.show_all_items()
        










