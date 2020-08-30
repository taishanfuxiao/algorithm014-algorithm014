'''46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result,path = [],[]
        def dfs(nums,path):
            if len(nums)==0:
                result.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[0:i]+nums[i+1:],path+list([nums[i]]))
        dfs(nums,path)
        return result