class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        l=0
        if not nums:
            return 0
        for x in s:
           if x-1 in s:
             continue
           size=1
           while x+size in s:
            size+=1
           l=max(size,l)
        return l
        
        
        