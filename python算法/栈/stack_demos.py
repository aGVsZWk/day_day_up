from stack import Stack


class StackDemos(object):
    def __init__(self):
        self.stack = Stack()

    def is_valid_paren(self, target):
        """括号匹配"""
        paren_dict = {")": "(", "}": "{", "]": "["}
        for i in target:
            if i not in paren_dict:
                self.stack.push(i)
            else:
                top_elem = self.stack.pop() if not self.stack.isEmpty() else "#"
                if paren_dict[i] != top_elem:
                    return False
        return True if self.stack.isEmpty() else False

import unittest

class StackDemosTest(unittest.TestCase):
    def setUp(self):
        self.target1 = "({}[])"
        self.target2 = "({}[)"
        self.target3 = "()"
        self.stack_demos1 = StackDemos()
        self.stack_demos2 = StackDemos()
        self.stack_demos3 = StackDemos()


    def test_valid_paren(self):
        result = self.stack_demos1.is_valid_paren(self.target1)
        self.assertEqual(True, result)
        result = self.stack_demos2.is_valid_paren(self.target2)
        self.assertEqual(False, result)
        result = self.stack_demos3.is_valid_paren(self.target3)
        self.assertEqual(True, result)

if __name__ == '__main__':
    unittest.main()
