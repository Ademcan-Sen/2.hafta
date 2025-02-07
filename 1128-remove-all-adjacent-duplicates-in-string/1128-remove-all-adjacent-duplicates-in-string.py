class Solution:
    def removeDuplicates(self, s: str) -> str:
        t = []
        for char in s:
            if t:
                if t[-1] == char:
                    t.pop()
                else:
                    t.append(char)
            else:
                t.append(char)
        result = ''.join(t)
        return result
        