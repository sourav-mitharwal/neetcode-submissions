class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for num in range(len(nums)):
            need = target - nums[num]
            if need in dic:
                return [dic[need],num]
            dic[nums[num]] = num