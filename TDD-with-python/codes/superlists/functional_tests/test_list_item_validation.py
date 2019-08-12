from .base import FunctionalTest
from unittest import skip


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
