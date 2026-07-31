class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s1 , f = 0 , 0
        while True:
            s1 = nums[s1]
            f = nums[nums[f]]
            if s1 == f:
                break
        s2 = 0
        while True:
            s1 = nums[s1]
            s2 = nums[s2]
            if s1 == s2 :
                return s1
        