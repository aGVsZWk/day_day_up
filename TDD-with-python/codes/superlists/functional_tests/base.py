from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
# import unittest
# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
import sys
from unittest import skip

MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            print(arg)
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.close()

    def check_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


class NewVisitorTest(StaticLiveServerTestCase):

    def test_case_start_a_list_for_one_user(self):
        # 测试首页标题和头部包含"To-Do"这个词
        self.browser.get(self.server_url)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-do', header_text)

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
        time.sleep(1)
        # 输入回车, 页面显示更新, 在待办事项列表中显示了'2: Use peacock feathers to make a fly'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly'
        )

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # 输入新的todo事项
        self.browser.get(self.server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        time.sleep(1)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 她注意到了他的待做事项在一个不同的URL中
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # 来了一个新用户, Francis
        # 退出浏览器, 用新的浏览器会话来保证cookies配置
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis访问了首页
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        # 首页没有之前用户的待做事项
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis开始输入新的待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        time.sleep(1)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy milk')

        # Francis获取到了它的待做事项不是之前的URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 然后本页面没有Francis的事项清单
        page_text = self.browser.find_element_by_tag_name('body').text
        # Francis的清单页没有之前用户的待做事项
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)


class LayoutAndStyingTest(FunctionalTest):
    pass
    # def test_layout_and_styling(self):
    #     # Edith goes to the home page
    #     self.browser.get(self.server_url)
    #     self.browser.set_window_size(1024, 768)
    #
    #     # She notices the input box is nicely centered
    #     inputbox = self.browser.find_element_by_id('id_new_item')
    #     self.assertAlmostEqual(
    #         inputbox.location['x'] + inputbox.size['width'] / 2,
    #         512,
    #         delta=5
    #     )
    #
    #     # She starts a new list and sees the input is nicely
    #     # centered there too
    #     inputbox.send_keys('testing')
    #     inputbox.send_keys(Keys.ENTER)
    #     self.wait_for_row_in_list_table('1: testing')
    #     inputbox = self.browser.find_element_by_id('id_new_item')
    #     self.assertAlmostEqual(
    #         inputbox.location['x'] + inputbox.size['width'] / 2,
    #         512,
    #         delta=5
    #     )


class ItemValidationTest(FunctionalTest):

    @skip
    def test_can_add_empty_list_items(self):
        # 测试是否能提交空事项
        # 伊迪斯访问首页, 不小心提交了一个空待办事项
        # 输入框中没输入内容, 他就按下了回车键

        # 首页刷新了, 显示一个错误消息
        # 提示待办事项不能为空

        # 他输入一些文字, 然后再次提交了, 这次没问题了

        # 他又提交了一个空待办事项

        # 他在清单页面又看到了类似的错误消息

        # 输入文字之后提交就没问题了

        self.fail('write me!')
