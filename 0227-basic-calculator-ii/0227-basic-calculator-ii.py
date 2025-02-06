class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operation = '+'
        s = s.replace(" ", "") 
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            if not char.isdigit() or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    stack[-1] = stack[-1] * current_number
                elif operation == '/':
                    stack[-1] = int(stack[-1] / current_number)
                operation = char
                current_number = 0
        return sum(stack)