from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import unittest
from django.test import LiveServerTestCase
import time


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.close()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_case_start_a_list_for_one_user(self):
        # 测试首页标题和头部包含"To-Do"这个词
        self.browser.get(self.live_server_url)
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
        # 输入回车, 页面显示更新, 在待办事项列表中显示了'1: Buy peacock feathers'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 再输入其它的待办事项并判断
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                         inputbox.get_attribute('placeholder'),
                         'Enter a to-do item'
        )
        # 她在一个文本输入框中输入了"Use peacock feathers to make a fly"(用孔雀羽毛做什么东西)
        inputbox.send_keys('Use peacock feathers to make a fly')
        time.sleep(3)
        # 输入回车, 页面显示更新, 在待办事项列表中显示了'2: Use peacock feathers to make a fly'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly'
            )

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # 输入新的todo事项
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 她注意到了他的待做事项在一个不同的URL中
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # 来了一个新用户, Francis
        # 退出浏览器, 用新的浏览器会话来保证cookies配置
        self.browser.quit()
        self.browser = webdriver.Firefix()

        # Francis访问了首页
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        # 首页没有之前用户的待做事项
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis开始输入新的待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('Buy milk')

        # Francis获取到了它的待做事项不是之前的URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 然后本页面没有Francis的事项清单
        page_text = self.browser.find_element_by_tag_name('body').text
        # Francis的清单页没有之前用户的待做事项
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)


# if __name__ == "__main__":
#     unittest.main()
