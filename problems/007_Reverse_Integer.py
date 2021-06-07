from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        result = []
        sign = 0
        for c in x:
            if c == '-':
                sign -= 1
                continue
            elif c == '+':
                sign += 1
                continue
            result.insert(0, c)
        if sign == -1:
            result.insert(0, '-')
        else:
            result.insert(0, '+')
        result = int(''.join(result))
        if ((result > 2147483647) or (result < -2147483648)):
            result = 0
        return result

solution = Solution()
print(solution.reverse(123))
