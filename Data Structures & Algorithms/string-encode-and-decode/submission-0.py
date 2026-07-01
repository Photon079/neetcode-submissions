class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for word in strs:
            ls=len(word)
            encoded+=str(ls)+"#"+word
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(s):
            j=i
            while(s[j]!="#"):
                j+=1
            length_strs=s[i:j]
            length=int(length_strs)
            word=s[j+1:j+1+length]
            decoded.append(word)
            i=j+1+length
        return decoded





