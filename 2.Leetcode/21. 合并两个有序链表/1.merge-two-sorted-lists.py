# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        list_ret = []
        
        while l1 or l2:
            
            if l1:
                list_ret.append(l1.val)
                l1 = l1.next
                
            if l2:
                list_ret.append(l2.val)
                l2 = l2.next
        
        return sorted(list_ret)
        