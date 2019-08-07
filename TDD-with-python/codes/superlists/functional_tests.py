from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.close()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_case_start_a_list_and_retrieve_it_later(self):
        # 测试首页标题和头部包含"To-Do"这个词
        self.browser.get('http://127.0.0.1:8001')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                         inputbox.get_attribute('placeholder'),
                         'Enter a to-do item'
        )
        # 她在一个文本输入框中输入了"Buy peacock feathers"(购买孔雀羽毛)
        inputbox.send_keys('Buy peacock feathers')
        time.sleep(1)
        # 输入回车, 页面显示更新, 在待办事项列表中显示了'Buy peacock feathers'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 再输入其它的待办事项并判断
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                         inputbox.get_attribute('placeholder'),
                         'Enter a to-do item'
        )
        # 她在一个文本输入框中输入了"Buy peacock feathers"(购买孔雀羽毛)
        inputbox.send_keys('2: Use peacock feathers to make a fly')
        time.sleep(1)
        # 输入回车, 页面显示更新, 在待办事项列表中显示了'Buy peacock feathers'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly'
            )

        self.fail('Finish the test')
        # 可以输入其他内容, 在做其它的事情


if __name__ == "__main__":
    unittest.main()
