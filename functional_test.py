from selenium import webdriver
import unittest


class OpenPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_open_page_and_see_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Karate', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
