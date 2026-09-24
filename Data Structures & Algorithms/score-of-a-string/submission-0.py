class Solution:
    def scoreOfString(self, s: str) -> int:
        j = 1
        su = 0
        for i in range(len(s)-1):
            su += abs(ord(s[i])- ord(s[j]))
            j+=1
        return su