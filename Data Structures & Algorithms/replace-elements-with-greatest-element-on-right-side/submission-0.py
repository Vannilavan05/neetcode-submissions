class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(1,len(arr)):
            a = 0 
            a = max(arr[i:])
            arr[i-1] = a
        arr[-1] = -1
        return arr