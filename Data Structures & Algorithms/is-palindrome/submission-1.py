class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = []
        for i in s:
            if i.isalnum():
                b.append(i.lower())
        left = 0
        right = len(b)-1
        while left < right:
            if b[left] != b[right]:
                return False
            left+=1
            right-=1
        return True