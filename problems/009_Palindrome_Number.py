import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        success = 1
        for i in range(math.floor(len(x) / 2)):
            if x[i] != x[-(i + 1)]:
                success = 0
                break
        return (success == 1)
solution = Solution()
print(solution.isPalindrome(1122332211))