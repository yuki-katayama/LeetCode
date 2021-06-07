from itertools import product
from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def inc_cut_index(list_c):
            i = 0
            for i, value in enumerate(list_c):
                list_c[i] = value + i
                i += 1
        def makeMap(h, w):
            map = [[0 for i in range(w + len(verticalCuts))] for j in range(h + len(horizontalCuts))]
            for height, width in product(range(len(map)), range(len(map[0]))):
                for hori in horizontalCuts:
                    if hori == height:
                        map[height][width] = 1
                for ver in verticalCuts:
                    if ver == width and map[height][width] == 0:
                        map[height][width] = 1
                    elif ver == width and map[height][width] == 1:
                        map[height][width] = 2
            return map
        def calc_area_rec(height, width):
            if height < 0 or width  < 0 or height >= len(map) or width >= len(map[0]) or map[height][width] != 0:
                return (0)
            map[height][width] = 1
            return 1 + calc_area_rec(height, width + 1) + calc_area_rec(height, width - 1) + calc_area_rec(height + 1, width) + calc_area_rec(height - 1, width)
        horizontalCuts = sorted(horizontalCuts)
        inc_cut_index(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        inc_cut_index(verticalCuts)
        map = makeMap(h, w)
        max = 0
        for height, width in product(range(len(map)), range(len(map[0]))):
            if (map[height][width] != 2):
                tmp  = calc_area_rec(height, width)
            if (max < tmp):
                max = tmp
        return max

h = 5
w = 4
solution = Solution()
hori_c = [3, 1]
ver_c = [1]
print(solution.maxArea(h, w, hori_c, ver_c))