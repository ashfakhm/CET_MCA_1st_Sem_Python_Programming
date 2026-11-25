"""Display Python book details using inheritance and method overriding."""


class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher:", self.name)


class Book(Publisher):
    def __init__(self, publisher_name, title, author):
        super().__init__(publisher_name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, publisher_name, title, author, price, no_of_pages):
        super().__init__(publisher_name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        super().display()
        print("Price:", self.price)
        print("Number of pages:", self.no_of_pages)


python_book = Python(
    input("Enter publisher name: "),
    input("Enter book title: "),
    input("Enter author name: "),
    float(input("Enter book price: ")),
    int(input("Enter number of pages: ")),
)
python_book.display()
