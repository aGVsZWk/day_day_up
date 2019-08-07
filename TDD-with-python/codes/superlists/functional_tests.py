from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.close()

    def test_case_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8001')
        self.assertIn('To-do', self.browser.title)


if __name__ == "__main__":
    unittest.main()
