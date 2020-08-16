class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            return nums2
        if n == 0:
            return nums1
        left,right = 0,0
        result = []
        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                result.append(nums1[left])
                left += 1
            if nums1[left] > nums2[right]:
                result.append(nums2[right])
                right += 1
        if left < m:
            result.append(nums1[left])
            left += 1
        if right < n:
            result.append(nums2[right])
            right += 1
        return result