from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from polls.models import Question, Choice
from django.template import loader


def index(request):
    return HttpResponse("welcome on my index page")


def hello(request):
    return HttpResponse("HELLO WORLD!!")


def questions_list(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    # template = loader.get_template('list.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/list.html', context)


def detail(request, question_id):
    try:
        questions = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    # template = loader.get_template('details.html')
    context = {
        'questions': questions
    }
    # return HttpResponse(template.render(context, request))
    return render (request, 'polls/details.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', context={'question':question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if question.pub_date > timezone.now():
        raise Http404

    choice_id = request.POST.get('choice')

    try:
        selected_choice = question.choice_set.get(pk=choice_id)
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {'questions': question, 'error message': "nie wybrano odpowiedzi"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



