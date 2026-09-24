class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        r = 0
        c = 0
        while r < len(nums):
            if nums[r] == 1:
                r+=1
            else:
                l = r+1
                r+=1
            c = max(c,r-l)
        return c