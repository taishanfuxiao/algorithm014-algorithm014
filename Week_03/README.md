学习笔记
回溯的最大收获：
1，回溯是一种算法思想，递归实现回溯的具体操作
2. 回溯的写法分为两种，
	a）在递归函数中传递全局参数（每一层是全局变量浅拷贝参数），实现参数随函数
	层数的变化；这种方法不需要显式的pop弹出全局变量中不合适的元素
def generateParenthesis1(self, n):
        if n == 0:
            return []
        result = []
        def dfs(n,left_nums,right_nums,result,path):
            if left_nums == n and right_nums == n:
                result.append(path)
                return
            if left_nums < n:
                
                dfs(n,left_nums+1,right_nums,result,path+'(')
            if right_nums < left_nums and right_nums < n:
                
                dfs(n,left_nums,right_nums+1,result,path +')')
                
        dfs(n,0,0,result,'')
        return result
	b）a的函数参数通过中间变量替换，但是中间变量名不能和函数参数一致
	class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []
        result = []
        def dfs(n,left_nums,right_nums,result,path):
            if left_nums == n and right_nums == n:
                result.append(path)
                return
            if left_nums < n:
                tmp = path + '(' #有中间变量 但不能写成 path=path + '(' 这样会导致递归层之间参数的相互干扰
                
                dfs(n,left_nums+1,right_nums,result,tmp)
            if right_nums < left_nums and right_nums < n:
                tmp1 = path +')'
                
                dfs(n,left_nums,right_nums+1,result,tmp1)
                
        dfs(n,0,0,result,'')
        return result
	c)回溯中参数pop与显示pop
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
问题：
回溯的剪枝操作不熟悉