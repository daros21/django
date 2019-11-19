
from faker import Faker
import datetime

from books.models import Author, Publisher, Book

faker = Faker("pl")

def generate_authors(n):
    for i in range(n):
        f_name = faker.first_name()
        l_name = faker.last_name()
        b_day = faker.date_of_birth()
        desc = faker.text(1000)
        Author.objects.create(first_name=f_name, last_name=l_name, birth_date=b_day, description=desc)
    print(f"Utworzono {n} autorow")


def generate_books(n):
    publishers = Publisher.objects.all()
    all_authors = Author.objects.all()
    for i in range(n):
        title = faker.text(20)
        pages = faker.random_int(10,300)
        price = faker.pydecimal(2,2, positive=True)
        rating = faker.pydecimal(1,2, positive=True)
        pub_date = faker.date_this_century()
        publisher = faker.random_choices(publishers, length=1)[0]
        authors = faker.random_choices(all_authors, length=faker.random_int(1, 3))

        book = Book(title=title, pages=pages, price=price, rating=rating, pub_date=pub_date, publisher=publisher)

        book.save()
        for a in authors:
            book.authors.add(a)


