class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if len(title) < 3:
            raise Exception("Title not valid!")
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if len(author.split()) == 2:
            last_name = author.split()[1]
            if last_name[0].isdigit():
                raise Exception("Author not valid!")
        self.__author = author

    @property
    def price(self):
        return f"{self.__price:.2f}"

    @price.setter
    def price(self, price):
        if price <= 0:
            raise Exception("Price not valid!")
        self.__price = price

    class_type = 'Book'

    def __str__(self):
        print(self.class_type)
        return f"Type: {self.class_type}\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price}"

class GoldenEditionBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author, price)
        self.price = price

    @property
    def price(self):
        return f"{self.__price:.2f}"

    @price.setter
    def price(self, price):
        if price <= 0:
            raise Exception("Price not valid!")
        self.__price = price * 1.30
    
    class_type = 'GoldenEditionBook'


author, title, price = input(), input(), float(input())

try:
    book = Book(title, author, price)
    golden_book = GoldenEditionBook(title, author, price)
    print(book)
    print()
    print(golden_book)
except Exception as error:
    print(error)
