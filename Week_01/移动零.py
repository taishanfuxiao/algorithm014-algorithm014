class Solution:
    # def moveZeroes(self, nums):
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     非零元素放到应该在的位置，然后补充零
    #     """
        
    #     length = len(nums)
    #     j = 0
    #     for i in range(length):
    #         if nums[i]!=0:
    #             nums[j] = nums[i]
    #             j+=1
    #             nums[i] = 0
                
    #     return nums
    def moveZeroes(self,nums):
        '''
        滚雪球方式：0元素收集到snowball里面，然后非零元素和雪球的最左边元素交换
        '''
        snowball = 0
        length = len(nums)
        for i in range(length):
            if nums[i]==0:
                snowball+=1
            else:
                nums[i-snowball],nums[i] = nums[i],nums[i-snowball]
        return nums