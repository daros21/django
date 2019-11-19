from django.urls import path

from books.views import book_list, book_detail
from polls import views
from polls.views import hello, questions_list, detail, results, vote

app_name = "books"
urlpatterns = [
    # /books/
    path("", book_list, name="list"),
    path("<int:book_id>", book_detail, name="details")
]