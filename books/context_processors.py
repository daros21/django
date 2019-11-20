from books.models import Notification


def books_context_processor(request):
    return {'important_message': "to jest bardzo wazna wiadomosc"}

def books_sales(request):
    note = ""
    if Notification.objects.first():
        note = Notification.objects.last().note

    context = {
        'note': note
    }
    return context