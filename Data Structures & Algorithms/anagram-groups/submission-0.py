class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in A:
                A[sorted_word].append(word)
            else:
                A[sorted_word] = [word]
        return list(A.values())      