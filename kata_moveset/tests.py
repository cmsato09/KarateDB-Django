from django.test import TestCase


class DelibrateFailTest(TestCase):

    def test_bad_math(self):
        self.assertEqual(1 + 1, 5)
