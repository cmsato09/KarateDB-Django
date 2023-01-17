from django.test import TestCase
from django.urls import resolve
from kata_moveset.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


# class DelibrateFailTest(TestCase):
#
#     def test_bad_math(self):
#         self.assertEqual(1 + 1, 5)
