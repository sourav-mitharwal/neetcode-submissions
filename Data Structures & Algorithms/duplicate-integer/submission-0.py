class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        separate_array = set();
        for n in nums:
            if n in separate_array:
                return True
            separate_array.add(n)
        return False
