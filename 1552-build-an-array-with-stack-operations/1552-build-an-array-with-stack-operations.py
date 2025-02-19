class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        t = set(target)
        result = []
        for i in range(1, target[-1] + 1):
            if i in t:
                result.append("Push")
            else:
                result.append("Push")
                result.append("Pop")
        return result
        