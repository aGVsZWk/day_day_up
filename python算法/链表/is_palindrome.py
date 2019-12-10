###
### 判断是否是回文字符串
###
from chain_table import ChainTable


def reverse(head):
    prev = None
    node = None
    next = head
    while next._next:
        prev = node
        node = next
        next = next._next
        node._next = prev
    next._next = node
    return next


def is_palindrome(target):
    slow = target.head
    fast = target.head
    j = 0
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
        j += 1
    reverse_node = reverse(slow)
    # while reverse_node:
    #     reverse_node = reverse_node._next
    head_node = target.head
    is_palin = True
    while (head_node and reverse_node):
        if (head_node.data == reverse_node.data):
            head_node = head_node._next
            reverse_node = reverse_node._next
        else:
            is_palin = False
            break
    return is_palin

if __name__ == '__main__':
    test_str1 = ChainTable()
    test_str2 = ChainTable()
    for i in "aabbcc":
        test_str1.append(i)
    for i in "aabbaa":
        test_str2.append(i)
    h = test_str1.head
    # while h:
    #     print(h.data)
    #     h = h._next
    print(is_palindrome(test_str1))
    print(is_palindrome(test_str2))
