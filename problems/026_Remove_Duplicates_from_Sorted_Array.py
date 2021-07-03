from typing import List

class Solution: #beats 66.36%
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        not_dup_i = 1
        before = nums[0]
        for i in range(1, len(nums)):
            if before == nums[i]:
                continue
            nums[not_dup_i] = nums[i]
            before = nums[not_dup_i]
            not_dup_i += 1
        return not_dup_i

class Solution: #beats 99.92%
    def removeDuplicates(self, nums: List[int]) -> int:
        n = sorted(list(set(nums)))
        for i in range(len(n)):
            nums[i] = n[i]
        return (len(n))

l = [-1,0,0,3]
solution = Solution()
print(solution.removeDuplicates(l), l)