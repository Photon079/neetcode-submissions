class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        for ch in s:
            if ch.isalnum():
                lower_ch = ch.lower()
                filtered.append(lower_ch)
        reverse_f= filtered[::-1]
        if reverse_f == filtered:
            return True
        else:
            return False
         



        