import random
from datetime import datetime


class Book:
    on_shelf = []
    on_loan = []

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}"

    def borrow(self):
        if self.lent_out():
            return False
        else:
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
            self.due_date = Book.current_due_date()
            return True

    def return_to_library(self):
        if self.lent_out():
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            self.due_date = None
            return True
        else:
            return False

    def lent_out(self):
        return self in Book.on_loan

    @classmethod
    def create(cls, title, author, isbn):
        book = Book(title, author, isbn)
        cls.on_shelf.append(book)
        return book

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    @classmethod
    def overdue_books(cls):
        overdue = []
        for book in cls.on_loan:
            if book.due_date < datetime.now():
                overdue.append(book)
        return overdue

    @classmethod
    def browse(cls):
        return random.choice(cls.on_shelf)


sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create(
    "If They Come in the Morning", "Angela Y. Davis", "0893880221"
)

print(Book.browse().title)
print(Book.browse().title)
print(len(Book.on_shelf))
print(len(Book.on_loan))
print(sister_outsider.lent_out())
print(sister_outsider.borrow())
print(len(Book.on_shelf))
print(len(Book.on_loan))
print(sister_outsider.lent_out())
print(sister_outsider.borrow())
print(sister_outsider.due_date)
print(len(Book.overdue_books()))
print(sister_outsider.return_to_library())
print(sister_outsider.lent_out())
print(len(Book.on_shelf))
print(len(Book.on_loan))
