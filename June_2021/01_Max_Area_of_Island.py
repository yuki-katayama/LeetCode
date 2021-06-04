from typing import List
from itertools import product
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, height, width = 0, len(grid), len(grid[0])
        def rec(h, w):
            if (h < 0 or w < 0 or h >= height or w >= width or grid[h][w] == 0):
                return 0
            grid[h][w] = 0
            return 1 + rec(h + 1, w) + rec(h - 1, w) + rec(h, w + 1) + rec(h, w - 1)
        for h, w in product(range(height), range(width)):
            if (grid[h][w] == 1):
                ans = max(ans, rec(h, w))
        return ans

Island = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
solution = Solution()
print(solution.maxAreaOfIsland(Island))
