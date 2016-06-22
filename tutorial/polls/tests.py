from django.test import TestCase
from django.utils import timezone

from .models import Question


class PollsTest(TestCase):
    def test_was_published_recently(self):
        obj = Question(pub_date=timezone.now())
        self.assertTrue(obj.was_published_recently())
