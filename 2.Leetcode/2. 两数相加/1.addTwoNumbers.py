# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """

        str_l1 = ""
        str_l2 = ""
        while l1.next or l2.next:
            if l1.next:
                str_l1 = str(l1.val) + str_l1
                l1 = l1.next
            if l2.next:
                str_l2 = str(l2.val) + str_l2
                l2 = l2.next
        else:
            str_l1 = str(l1.val) + str_l1
            str_l2 = str(l2.val) + str_l2

        str_ret = str(int(str_l2) + int(str_l1))

        list_ret = []

        for foo in list(str_ret):
            list_ret.append(int(foo))
        list_ret.reverse()

        return list_ret






