class Solution:
    def minimumLength(self, s: str) -> int:
        l,r = 0, len(s) - 1
        
        while l < r and s[l] == s[r]:
            k = s[l]
            while l <= r and s[l] == k:
                l += 1
            while r >= l and s[r] == k:
                r -= 1
        
        return (r - l + 1)

        