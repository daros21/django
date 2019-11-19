from django.urls import path

from books.views import books_list, book_details, BookList, BookDetail

app_name = "books"
urlpatterns = [
    path("", BookList.as_view(), name="list"),
    path("<int:pk>", book_details, name="details"),
    path("generic/<int:pk>", BookDetail.as_view(), name="details_generic")
]