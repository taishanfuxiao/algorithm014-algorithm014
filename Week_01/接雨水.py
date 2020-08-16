class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length == 0:
            return 0
        left,right = [0]*length,[0]*length
     
        for i in range(1,length):
            left[i] = max(left[i-1],height[i-1])
        for i in range(length-2,-1,-1):
            right[i] = max(right[i+1],height[i+1])
        water = 0
        for j in range(length):
            level = min(left[j],right[j])
            water += max(0,level-height[j])
        return water