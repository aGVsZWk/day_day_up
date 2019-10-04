class OldCourse(object):
    """老的课程类"""
    def show(self):
        """显示关于本课程的所有信息"""
        print("show description")
        print("show teacher of course")
        print("show labs")


class Page(object):
    """使用课程对象的客户端"""
    def __init__(self, course):
        self.course = course

    def render(self):
        self.course.show()


class NewCourse(object):
    """新的课程类"""
    def show_desc(self):
        print("show description")

    def show_teachers(self):
        print("show teacher of course")

    def show_labs(self):
        print("show labs")


class Adapter(object):
    """适配器, 实现新的课程类兼容老的课程show方法"""
    def __init__(self, course):
        self.course = course

    def show(self):
        """适配方法, 调用真正的操作"""
        self.course.show_desc()
        self.course.show_teacher()
        self.course.show_labs()


if __name__ == '__main__':
    old_course = OldCourse()
    page = Page(old_course)
    page.render()

    new_course = NewCourse()
    # 新课程进行适配
    # page(new_course)  # 新的课程没有show方法, 无法进行适配, 对其加适配器
    adapter = Adapter(new_course)
    page = Page(adapter)
    page.render()
