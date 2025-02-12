class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        sayi = (float('inf'))
        count = {}
        l = 0
        for r in range(len(blocks)):
            count[blocks[r]] = 1 + count.get(blocks[r], 0)
            while r - l + 1 > k:
                count[blocks[l]] -= 1
                l += 1
            if r - l + 1 == k:
                sayi = min(sayi, count.get('W', 0))
        return sayi
        if not blocks:
            return 0