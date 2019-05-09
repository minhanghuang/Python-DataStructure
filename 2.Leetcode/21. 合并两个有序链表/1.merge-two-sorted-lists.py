"""
https://leetcode-cn.com/problems/merge-two-sorted-lists/submissions/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        list_node = []

        if l1:
            while l1.next:

                if l1.next:
                    list_node.append(l1.val)
                    l1 = l1.next
            else:
                list_node.append(l1.val)
        if l2:
            while l2.next:

                if l2.next:
                    list_node.append(l2.val)
                    l2 = l2.next
            else:
                list_node.append(l2.val)

        list_node = sorted(list_node)

        return list_node