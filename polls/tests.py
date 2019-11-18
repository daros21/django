import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice


def create_question(question_text: str, days: int):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date = time)


class QuestionModelsTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No questions')

    def test_past_question(self):
        create_question(question_text='past_question', days=-30)
        response = self.client.get(reverse('polls:list'))
        self.assertQuerysetEqual(response.context['questions'], ['<Question: past_question>'])

    def test_future_question(self):
        create_question(question_text='future question', days=30)
        response = self.client.get(reverse('polls:list'))
        self.assertContains(response, '<div id="error">No questions</div>')

    def test_future_and_past_question(self):
        create_question(question_text="future question", days=30)
        create_question(question_text="past question", days=-30)
        response = self.client.get(reverse('polls:list'))
        self.assertQuerysetEqual(response.context['questions'], ['<Question: past question>'])

    def test_only_three_questions(self):
        create_question(question_text="past question 1", days=-5)
        create_question(question_text="past question 2", days=-6)
        create_question(question_text="past question 3", days=-7)
        create_question(question_text="past question 4", days=-8)
        response = self.client.get(reverse('polls:list'))
        self.assertQuerysetEqual(
            response.context['questions'],
            [
                '<Question: past question 1>'
                '<Question: past question 2>'
                '<Question: past question 3>'
            ]
        )

class QuestionDetailViewTest(TestCase):

    def test_future_question(self):
        future_question = create_question('future question', 10)
        url = reverse('polls:detail', args=(future_question.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question('past question', -20)
        url = reverse('polls:detail', args=(past_question.id, ))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

class QuestionResultViewTest(TestCase):

    def test_future_question(self):
        future_question = create_question('future question', 10)
        url = reverse('polls:results', args=(future_question.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_past_question(self):
        past_question = create_question('past question', -20)
        url = reverse('polls:results', args=(past_question.id, ))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionVoteViewTest(TestCase):

    def test_can_not_vote_for_future_question(self):
        future_question = create_question('future question', 10)
        choice = Choice.objects.create(choice_text = "aaa", question=future_question)
        url = reverse('polls:vote', args=(future_question.id, ))
        form = {'choice': choice.id}
        response = self.client.post(url, data=form)
        self.assertEqual(response.status_code, 404)
