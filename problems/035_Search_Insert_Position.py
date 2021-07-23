from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if (target <= nums[0]):
            return 0
        for i in range(0, len(nums) - 1):
            if (nums[i] <= target and target <= nums[i + 1]):
                return i + 1
        return len(nums)

nums = [1,3,5,6]
target = 0
solution = Solution()
print(solution.searchInsert(nums, target))