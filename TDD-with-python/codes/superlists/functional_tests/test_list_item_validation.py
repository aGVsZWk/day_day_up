from .base import FunctionalTest
from unittest import skip
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):

    def test_can_add_empty_list_items(self):
        # 测试是否能提交空事项

        # 伊迪斯访问首页, 不小心提交了一个空待办事项
        # 输入框中没输入内容, 他就按下了回车键
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        # 首页刷新了, 显示一个错误消息
        # 提示待办事项不能为空
        error = self.browser.find_element_by_css_selector('.has-error')
        # self.assertEqual(error.text, "You can't have an empty list item")
        self.wait_for(lambda: self.assertEqual(
                error.text, "You can't have an empty list item"))
        # 他输入一些文字, 然后再次提交了, 这次没问题了
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')
        # 他又提交了一个空待办事项
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        # 他在清单页面又看到了类似的错误消息
        error = self.browser.find_element_by_css_selector('.has-error')
        # self.assertEqual(error.text, "You can't have an empty list item")
        self.wait_for(lambda: self.assertEqual(
            error.text, "You can't have an empty list item"))
        # 输入文字之后提交就没问题了
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
        self.fail('finish this test!')
