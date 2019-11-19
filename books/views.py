from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, FormView, DetailView

from books.forms import CommentForm
from books.models import Book



class BookList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/list.html'
    paginate_by = 10

class BookDetail(DetailView, FormView):
    model = Book
    template_name = 'books/details.html'
    form_class = CommentForm



def books_list(request):
    books = Book.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(books, 10)
    books = paginator.get_page(page)
    return render(
        request,
        "books/list.html",
        context={'books': books})


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    form = CommentForm()

    return render(request, "books/details.html", {'book':book, 'form':form})

# POST books/1/comment
@require_http_methods(["POST"])
def book_comment(request, pk):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        book=Book.objects.get(pk=pk)
        comment.book=book
        comment.save()
        return HttpResponseRedirect(reverse('books:details', args=(pk,)))