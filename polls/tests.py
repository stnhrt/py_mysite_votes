
import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Question


# Create your tests here.
class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_old_question(self):
        """
        只要是超过1天的问卷，返回False
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        最近一天内的问卷，返回True
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
