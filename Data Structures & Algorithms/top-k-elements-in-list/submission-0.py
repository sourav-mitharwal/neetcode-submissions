class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # Count frequencies
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Put numbers into buckets
        for n, c in count.items():
            freq[c].append(n)

        # Collect top k frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res