from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = len(intervals)
        i = 0
        while(i < count):
            for j, array_sub in enumerate(intervals):
                if(i == j):
                    continue
                else:
                    if(intervals[i][0] >= array_sub[0] and intervals[i][1] <= array_sub[1]):
                        print(intervals[i], array_sub)
                        intervals.pop(i)
                        count -= 1
                        i -= 1
                        break
            i += 1
        return count


num = int(input())
my_class = Solution()
lst1 = [list(map(int, input().split())) for _ in range(num)]
my_list = my_class.removeCoveredIntervals(lst1)
print(my_list)
