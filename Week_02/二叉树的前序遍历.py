# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:   
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        val_ = []
        node = []
        while root is not None or len(node)>0:
            if root is not None:
                node.append(root)
                val_.append(root.val)
                root = root.left
                
            else:
                root = node.pop()
                root = root.right
        return val_