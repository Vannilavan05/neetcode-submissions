class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp =0
        l =0
        for i in range(len(s)):
            found= False
            for j in range(temp, len(t)):
                if s[i] == t[j] :
                    temp = j+1
                    l+=1
                    found = True
                    break
            if not found:
                return False
        return True

        