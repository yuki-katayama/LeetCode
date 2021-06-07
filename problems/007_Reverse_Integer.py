class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x = int('-' + ''.join(x[:0:-1]))
        else:
            x = int(x[::-1])
        if ((x > 2147483647) or (x < -2147483648)):
            x = 0
        return x

solution = Solution()
print(solution.reverse(-123))
