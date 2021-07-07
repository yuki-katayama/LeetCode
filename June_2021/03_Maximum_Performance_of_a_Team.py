from typing import List
from heapq import heappush, heappop

#1. start sorted from highest efficiency
#2. if the lowest speed, exec pop

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        sm, ans, heap = 0, 0, []
        for eff, speed_ in sorted(zip(efficiency, speed))[::-1]: #combine efficiency and speed eatch othre the some index and sort by efficiency
            if len(heap) > k - 1:
                sm -= heappop(heap) #heappop: delete the lowest value index
            heappush(heap, speed_)
            sm += speed_
            ans = max(ans, sm * eff)
        return ans % (10**9 + 7)

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 3
solution = Solution()
print(solution.maxPerformance(n, speed, efficiency, k))
