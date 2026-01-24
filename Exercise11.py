class Author:
    def __init__(self, fullname, email):
        self.fullname = fullname
        self.email = email


class Book:
    def __init__(self, title, authors, price, copy):
        self.title = title
        self.authors = authors
        self.price = price
        self.copy = copy

    def print_full_title(self):
        name_string = ""
        for i in range(len(self.authors) - 1):
            name_string = name_string + self.authors[i].fullname + ","
        name_string = name_string + self.authors[-1].fullname
        print(f"Title: {self.title}\nAuthors: {name_string}")

    def add_author(self, new_author):
        self.authors.append(new_author)


author1 = Author("John Smith", "g_poly@yahoo.com")
author2 = Author("Maria Papadopoulou", "g_poly2@yahoo.com")
author3 = Author("Alex Johnson", "g_poly3@yahoo.com")
author4 = Author("Alexis Panagiotis", "g_poly8@yahoo.com")
book1 = Book("Introduction to Programming", [
    author1,
    author2,
    author3,
    author4
], 24.99, 15000)

book1.print_full_title()
book1.add_author(Author("Tom Rossbow","tom@pcookbk.com"))
book1.print_full_title()