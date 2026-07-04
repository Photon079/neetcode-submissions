class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls=len(s)
        lt=len(t)
        if ls!=lt:
            return False

        count = [0]*26
        for i in range(ls):
            count[ord(s[i])-ord('a')] +=1
            count[ord(t[i])-ord('a')] -=1
        for val in count:
            if val!=0:
                return False

        return True



                

        