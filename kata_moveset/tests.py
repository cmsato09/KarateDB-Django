from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from kata_moveset.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith("<html>"))
        self.assertIn('<title>Karate Kata Database</title>', html)
        self.assertTrue(html.endswith('</html>'))

# class DelibrateFailTest(TestCase):
#
#     def test_bad_math(self):
#         self.assertEqual(1 + 1, 5)
