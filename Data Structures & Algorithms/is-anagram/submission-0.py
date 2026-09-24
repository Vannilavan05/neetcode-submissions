class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            a = list(s)
            a.sort()
            b = list(t)
            b.sort()
            for i in range(len(s)):
                if a[i]!= b[i]:
                    return False
        return True 