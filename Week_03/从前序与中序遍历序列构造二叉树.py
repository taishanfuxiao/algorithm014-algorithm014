'''
二叉树的序列化和反序列化
@序列化的过程使用层次遍历，节点为空的用‘null’补齐，这样成为了一个满二叉树，输出为list
@反序列化，使用队列记录顶点，同时用i指示序列化后的元素位置；因为是满二叉树，节点的左右节点都存在(不存在的是‘null’标记)
    因此遍历序列化后的list，还原二叉树
注意：反序列和序列化 使用的方法必须一致(层次遍历的序列化，则反序列化是也要层次法；前序遍历的序列化则使用前序遍历反序列化)
'''
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
# 式重构得到原数据。 
# 
#  请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
# 反序列化为原始的树结构。 
# 
#  示例: 
# 
#  你可以将以下二叉树：
# 
#     1
#    / \
#   2   3
#      / \
#     4   5
# 
# 序列化为 "[1,2,3,null,null,4,5]" 
# 
#  提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这
# 个问题。 
# 
#  说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。 
#  Related Topics 树 设计 

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
     '''
     层次遍历序列化和反序列化
     '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:return '[]'
        from collections import deque
        stack_node = deque()
        stack_node.append(root)
        serialize_r = []
        
        while stack_node:
            node = stack_node.popleft()
            if node is None:
                serialize_r.append('null')
            else:
                serialize_r.append(str(node.val))
                stack_node.append(node.left)
                stack_node.append(node.right)
        return '['+','.join(serialize_r) + ']'
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=='[]':
            return None
        from collections import deque
        node_str = split(',',data[1:-1])
        i  = 1
        root = TreeNode(int(node_str[0]))
        recode_node = deque()
        recode_node.append(root)
        while recode_node:
            node = recode_node.popleft()
            if node_str[i]!='null':
                node.left = TreeNode(int(node_str[i]))
                recode_node.append(node.left)
            i += 1
            if node_str[i] != 'null':
                node.right = TreeNode(int(node_str[i]))
                recode_node.append(node.right)
            i += 1
        return root      
   
 class Codec:
 '''
 前序遍历序列化和反序列化
 '''
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')

        vals = []
        doit(root)

        return ' '.join(vals)

    def deserialize(self, data):
        vals = split(' ', data)

        # vals = iter(vals)
        def doit(vals):
            # val = next(vals)
            val = vals.pop(0) #元素不断后移
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit(vals)
            node.right = doit(vals)
            return node

        return doit(vals)
                