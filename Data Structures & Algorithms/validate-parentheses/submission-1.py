class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        dic = {
            ")" : "(" ,
            "]" : "[" , 
            "}" : "{"
        }
        for i in s:
            if i in dic:
                if stk and stk[-1] == dic[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        return len(stk) == 0