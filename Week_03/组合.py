'''
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result,path = [],[]
        start = 1
        def dfs(start,result,path):
            if len(path)==k :
                result.append(path)
                return
            for i in range(start,n+1):
                # path = path+[i]
                dfs(i+1,result,path+[i]) #path每一层时都被浅层复制，不合适的元素不会被复制进来
                # path.pop()
        dfs(start,result,path)
        return result
 '''
 path作为全局变量，不合适的元素需要经过pop()清除，更像回溯的写法
 '''   
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result,path = [],[]
        start = 1
        def dfs(start,result,path):
            if len(path)==k :
                result.append(path[:])
                return
            for i in range(start,n+1):
                path = path+[i]
                dfs(i+1,result,path) 
                path.pop()#没有经过if返回说明不符合条件，需要弹出进入的元素
        dfs(start,result,path)
        return result
        