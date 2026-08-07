# 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s = {}
        dic = {}
        for i in range(len(s)):
            dic_s[s[i]] = dic_s.get(s[i], 0) + 1
            dic[t[i]] = dic.get(t[i], 0) + 1

        return dic_s == dic