class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []  
        gruplar = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                start = stack.pop()
            if not stack:
                gruplar.append(s[start:i+1])
        temiz_s = "".join([grup[1:-1] for grup in gruplar])
        return temiz_s

        
        