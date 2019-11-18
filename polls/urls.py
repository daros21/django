from django.urls import path

from polls import views
from polls.views import hello, questions_list, detail, results, vote

app_name = "polls"
urlpatterns = [
    # /polls/
    path("", questions_list, name="list"),
    # /polls/5/
    path("<int:question_id>/", detail, name="detail"),
    # /polls/5/results
    path("<int:question_id>/results/", results, name="results"),
    # /polls/5/vote
    path("<int:question_id>/vote", vote , name="vote"),
]