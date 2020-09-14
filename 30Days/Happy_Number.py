class Solution:
    def isHappy(self, n: int) -> bool:
        if(n == 1):
            return
        nums = map(int, str(n))
        # nums = (list(str(n)))
        # for i in range(len(nums)):
        #     nums[i] = int(nums[i])
        sum = 0
        for i in nums:
            sum += i**2
        self.isHappy(sum)
        return True


a = int(input())
fun = Solution()
print(fun.isHappy(a))
