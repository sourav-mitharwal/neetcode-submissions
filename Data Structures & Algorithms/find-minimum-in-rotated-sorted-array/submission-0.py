class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = 0
        while r > l :
            m = (r + l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]