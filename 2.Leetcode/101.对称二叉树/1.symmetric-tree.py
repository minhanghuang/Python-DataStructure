# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True
        queue_node_l = [root.left]
        queue_node_r = [root.right]

        while queue_node_l or queue_node_r:

            node_l = queue_node_l.pop()
            node_r = queue_node_r.pop()

            if (not node_l) and (not node_r):
                continue
            elif (node_l) and (not node_r):
                return False
            elif (not node_l) and (node_r):
                return False
            elif node_l.val != node_r.val:
                return False
            else:
                pass

            queue_node_l.insert(0, node_l.left)
            queue_node_l.insert(0, node_l.right)
            queue_node_r.insert(0, node_r.right)
            queue_node_r.insert(0, node_r.left)

        return True
