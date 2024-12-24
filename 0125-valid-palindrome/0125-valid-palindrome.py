class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        r=""
        for i in s:
            if i.isalnum():
                r=r+i
        k=r[::-1]
        if r==k:
            return True
        else:
            return False
                