# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        queue_val = []
        list_val_p = []
        queue_val.insert(0, p)
        while queue_val:
            node_p = queue_val.pop()
            if not node_p:
                list_val_p.append(" ")
                continue
            list_val_p.append(node_p.val)
            queue_val.insert(0, node_p.left)
            queue_val.insert(0, node_p.right)

        list_val_q = []
        queue_val.insert(0, q)
        while queue_val:
            node_q = queue_val.pop()
            if not node_q:
                list_val_q.append(" ")
                continue
            list_val_q.append(node_q.val)
            queue_val.insert(0, node_q.left)
            queue_val.insert(0, node_q.right)

        return True if list_val_p == list_val_q else False

