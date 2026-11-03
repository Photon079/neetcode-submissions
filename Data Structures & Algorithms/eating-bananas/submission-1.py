import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        
        while l<r:
            k=(l+r)//2
            th=0
            for num in piles:
                th+= math.ceil(num/k)
            if th<=h:
                r=k
            else :
                l=k+1
        return r
