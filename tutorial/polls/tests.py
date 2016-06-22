from datetime import timedelta

from django.shortcuts import resolve_url
from django.test import TestCase
from django.utils import timezone

from .models import Question


class PollsTest(TestCase):
    def test_was_published_recently(self):
        # 1日よりも少しだけ古い
        obj = Question(pub_date=timezone.now() - timedelta(days=1, minutes=1))
        self.assertFalse(obj.was_published_recently(), '1日と1分前に公開')

        # 1日よりも少しだけ新しい
        obj = Question(pub_date=timezone.now() - timedelta(days=1) + timedelta(minutes=1))
        self.assertTrue(obj.was_published_recently(), '1日と1分後に公開')

        # つい最近公開
        obj = Question(pub_date=timezone.now() - timedelta(minutes=1))
        self.assertTrue(obj.was_published_recently(), '1分前に公開')

        # もうちょっとしたら公開
        obj = Question(pub_date=timezone.now() + timedelta(minutes=1))
        self.assertFalse(obj.was_published_recently(), '1分後公開')


class ViewTest(TestCase):
    def test_index(self):
        response = self.client.get(resolve_url('polls:index'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.context['questions'].count())

        Question.objects.create(
            question_text='aaa',
            pub_date=timezone.now(),
        )
        response = self.client.get(resolve_url('polls:index'))
        self.assertEqual(1, response.context['questions'].count())

        self.assertEqual('aaa', response.context['questions'].first().question_text)
