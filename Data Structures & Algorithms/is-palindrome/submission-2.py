class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        for ch in s:
            if ch.isalnum():
                lower_ch = ch.lower()
                filtered.append(lower_ch)
        if filtered[::-1]== filtered:
            return True
        else:
            return False
         



        