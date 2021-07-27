from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        cmpareare = 0
        left = 0
        right = len(height) - 1
        while True:
            if (left == right):
                break
            else:
                mini = min(height[left], height[right])
                cmpare = (right - left) * mini
                if (mini == height[left]):
                    left += 1
                else:
                    right -= 1
                if (cmpare > max):
                    max = cmpare
        return max

solution = Solution()
print(solution.maxArea(height))