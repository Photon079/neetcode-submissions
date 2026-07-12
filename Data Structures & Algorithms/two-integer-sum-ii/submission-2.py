class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for x,num in enumerate(numbers):
            comp=target-num
            if comp in seen:
                return[seen[comp]+1,x+1]
            seen[num]=x
        return[ ]

        