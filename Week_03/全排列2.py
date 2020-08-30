class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result,path = [],[]
        def dfs(nums,path):
            if len(nums)==0 and path not in result:
                result.append(path)
                result 
            for i in range(len(nums)):
                dfs(nums[0:i]+nums[i+1:],path+list([nums[i]]))
        dfs(nums,path)
        return result