class Book:
    def __init__(self, title, author, chapters, price):
        self.title = title
        self.author = author
        self.chapters = list(chapters)
        self.price = price

    def __str__(self):
        return f"SOLD: {self.title} with author {self.author}. Chapters in the book {len(self.chapters)}"



def create_book(data):
    book_data = data.split(' -> ')[0]
    chapters = data.split(' -> ')[1].split(', ')

    try:
        title, author, price = book_data.split()
        price = float(price)
        if float(price) <= 0:
            return
        return Book(title, author, chapters, price)
    except:
        pass

    
def sell_book(data, books):
    if not data in list(map(lambda book: book.title, books)):
        print("No such book here")
        return

    return list(filter(lambda b: b.title == data, books))[0]


books = []

data = input()
while data != 'on work':
    book = create_book(data)
    if book:
        books.append(create_book(data))
    data = input()

sold_books = []
data = input()
while data != 'end work':
    book = sell_book(data, books)

    if book:
        sold_books.append(book)

    data = input()

if len(sold_books) == 0:
    print("Bad day :(")
else:
    [print(book) for book in sold_books]
    print(f"Money: {sum(list(map(lambda b: b.price, sold_books))):.2f}")