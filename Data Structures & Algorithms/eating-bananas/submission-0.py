class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        while l < r :
            m = (r+l) // 2

            ho = 0
            for p in piles:
                ho += (p + m - 1) // m
            if ho <= h:
                r = m
            else:
                l = m + 1
        return l

        