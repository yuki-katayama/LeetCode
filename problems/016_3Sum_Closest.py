from typing import List
import itertools

# Time Limit Exceeded
# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         all = itertools.combinations(nums, 3)
#         output = None
#         for x in all:
#             if(output == None or (abs((x[0] + x[1] + x[2]) - target) < abs(output - target))):
#                 output = (x[0] + x[1] + x[2])
#         return output

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length, output = len(nums), float("inf")
        for i in range(length):
            left, right = i + 1, length - 1
            while (left < right):
                current_v = nums[i] + nums[left] + nums[right]
                # output = min(output, current_v, key = lambda x: abs(x - target))
                if (abs(output - target) > abs(current_v - target)):
                    output = current_v
                if (current_v - target == 0):
                    return output
                if (current_v < target):
                    left += 1
                elif current_v > target:
                    right -= 1
        return output

array = [-1, 2, 1, -4]
target = 1
solution = Solution()
print(solution.threeSumClosest(array, target))