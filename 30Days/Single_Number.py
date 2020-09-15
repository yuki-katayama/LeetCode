import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        num = min(c, key=c.get)
        return num


nums = [4, 1, 2, 1, 2]
s = Solution()
num = s.singleNumber(nums)
print(num)

# List : 型ヒント
# https://note.nkmk.me/python-function-annotations-typing/
