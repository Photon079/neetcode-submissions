class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        area=0
        while i<j:
          l=min(heights[i],heights[j])
          b=j-i
          a=l*b
          area=max(a,area)
          
          if heights[i]<heights[j]:
            i+=1
          else:
            j-=1
        return area






        