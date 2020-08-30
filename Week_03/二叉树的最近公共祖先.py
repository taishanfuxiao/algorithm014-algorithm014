'''
二叉树的最近公共祖先
@方法一：树递归。分三种情况：1）节点 p,q分别在左右子树，则公共祖先为根节点；2）节点p,q都在左子树，则公共祖先为p或q(从上到下第一个节点)；
    3）节点p,q都在右子树，则公共祖先为p或q(从上到下第一个节点)；；因此，遍历所有的节点后，根据p,q是分别 在左右子树，都在右子树或者都在左子树判断公共祖先(后续遍历)
@方法二：从根节点到节点 p，q路径的第一个公共节点 就是最近的公共的祖先。寻找节点的路径时：如果当前节点的左右子节点均不存在指定值，则不能保存该节点
'''
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 
# 
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。” 
# 
#  例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4] 
#  示例 1: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#  
# 
#  示例 2: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

#  说明: 
# 
#  
#  所有节点的值都是唯一的。 
#  p、q 为不同节点且均存在于给定的二叉树中。 
#  
#  Related Topics 树 


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    输入的参数 p,q是节点，而不是节点的值
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root            
        left  = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left is None:#p,q都在右子树
            return right
        if right is None:#p,q都在左子树
            return left
        return root #p,q分别在左右子树
        
# leetcode submit region end(Prohibit modification and deletion)
class Solution:
    '''
    输入的参数 p,q是节点，而不是节点的值
    '''       
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p,path_q = [],[]
        def dfs(root,node,path):
            if root is None:
                return False
            path.append(root)
            if root==node :
                return True 
            if dfs(root.left,node,path) or dfs(root.right,node,path): #只找一条符合条件的路径即可
                return True
            path.pop() #左和右节点都不存在时，当前节点不符合条件，弹出
        dfs(root,p,path_p)
        dfs(root,q,path_q)
        ancestor_index  = 0
        i = 0
        r = 0
        while i<len(path_p) and i<len(path_q) and path_p[i] == path_q[i]:
            r = path_q[i]
            i += 1
        return r