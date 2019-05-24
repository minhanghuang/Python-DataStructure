# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        h = ListNode(x=None)
        h.next = head
        p = head
        list_ret = []
        while p:

            if h.val != p.val:  # 头指针和p指向的val不等
                list_ret.append(p.val)
                h = p  # 头指针走到p的位置
            else:  # 相等, 把p当前指向的节点断开
                if p.next:  # p当前指向的节点不是尾节点
                    h.next = p.next
                else:  # p当前指向的是尾节点
                    h.next = None

            p = p.next

        return list_ret
