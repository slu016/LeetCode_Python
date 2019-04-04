'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 0 -> 8
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def println(self):
        p = self
        while p is not None:
            print(p.val)
            p = p.next



def _addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    p = dummy = ListNode(-1)
    carry = 0
    while l1 and l2:
        p.next = ListNode(l1.val + l2.val + carry)
        carry = p.next.val // 10
        p.next.val %= 10
        p = p.next
        l1 = l1.next
        l2 = l2.next
    return dummy.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(5)
    r = _addTwoNumbers(l1, l2)
    r.println()
