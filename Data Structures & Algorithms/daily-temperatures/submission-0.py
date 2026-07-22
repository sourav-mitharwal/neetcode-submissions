class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        a = [0] * len(t)
        stack = []
        for i in range(len(t)):
            while stack and t[i] > t[stack[-1]]:
                prev = stack.pop()
                a[prev] = i - prev
            stack.append(i)
        return a
    
        