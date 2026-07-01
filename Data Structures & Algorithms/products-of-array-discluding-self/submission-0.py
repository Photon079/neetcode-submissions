class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=1
        result0=1
        output=[]
        zc=0
        for num in nums:
            if num==0:
                zc+=1
            else:   
                result*=num
        for i in range(len(nums)):
            if zc>1:
                output.append(0)
            elif zc==1:
                if nums[i] == 0:
                    output.append(result)
                else:
                    output.append(0)
            else:
                output.append((result//nums[i]))
        return output

            
        