class Solution:
    '''
    层次遍历的基本写法，所有的节点是一个list
    @ 使用了pre指示上一层的节点个数；next_layer_nums指示下一层的节点个数
    '''
    def levelOrder(self, root: 'Node') -> List[int]:
        from collections import deque
        queue = deque()
        queue.append(root)
        pre = 1
        next_layer_nums = 0
        result = []
        while queue:
            level = []
            while pre >0:
                pre -=1
                root = queue.popleft()
                level.append(root.val)
                for node in root.children:
                    if node is not None:
                        queue.append(node)
                        next_layer_nums += 1
            result.append(level)
            pre = next_layer_nums
            next_layer_nums = 0
                    
        return result