from django.test import TestCase


class PollsTest(TestCase):
    def test_success(self):
        self.assertEqual(1, 1)
        self.assertEqual(1, True)

    def test_failed(self):
        self.assertNotEqual(0, False)
