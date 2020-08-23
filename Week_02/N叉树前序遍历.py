class Solution:

    def preorder(self, root: 'Node') -> List[int]:
        result = [] #全局的list
        def helper(root):
            if root is None:
                return
            result.append(root.val)
            for node in root.children:
                helper(node)
        helper(root)
        return result