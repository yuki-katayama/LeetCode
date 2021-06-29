from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for c in s:
            if (c == '(' or c == '[' or c == '{'):
                l.append(c)
            elif c == ')' and (len(l) == 0 or l.pop() != '('):
                return False
            elif c == ']' and (len(l) == 0 or l.pop() != '['):
                return False
            elif c == '}' and (len(l) == 0 or l.pop() != '{'):
                return False
        if len(l) == 0:
            return True
        return False

solution = Solution()
print(solution.isValid("]"))