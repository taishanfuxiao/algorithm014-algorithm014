class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length ==0:
            return []
        hash_ = dict()
        for i in range(length):           
            tmp = target - nums[i]
            if tmp in hash_.keys():
                return [i,hash_.get(tmp)]
            else:
                hash_[nums[i]] = i