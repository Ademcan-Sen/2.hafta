class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == s[right]:
            k = s[left]
            while left <= right and s[left] == k:
                left += 1
            while right >= left and s[right] == k:
                right -= 1
        
        return right - left + 1

        