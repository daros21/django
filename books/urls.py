from django.urls import path

from books.views import books_list, book_details, BookList, BookDetail, book_comment, books_to_excel

app_name = "books"
urlpatterns = [
    # path("", BookList.as_view(), name="list"),
    path("", books_list, name="list"),
    path("<int:pk>", book_details, name="details"),
    path("generic/<int:pk>", BookDetail.as_view(), name="details_generic"),
    path("<int:pk>/comment", book_comment, name='comment'),
    path("report/", books_to_excel, name='report'),
]