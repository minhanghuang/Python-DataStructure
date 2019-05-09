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

        list_node = [] # 存储链表的数据(无序)

        if l1: # 如果链表l1不为空
            while l1.next: # 循环l1

                if l1.next:
                    list_node.append(l1.val) # 把数据添加到列表中
                    l1 = l1.next # 指向下一个节点
            else:
                list_node.append(l1.val) # 把最后的那个节点的数据也加到列表中
        if l2:
            while l2.next:

                if l2.next:
                    list_node.append(l2.val)
                    l2 = l2.next
            else:
                list_node.append(l2.val)

        list_node = sorted(list_node) # 排序

        return list_node