from typing import List
import collections

# Ver.1
# class Solution:
#     my_list = []
#     def findPairs(self, nums: List[int], k: int) -> int:
#         my_list = []
#         dup_mem = []
#         for i, num1 in enumerate(nums):
#             for j, num2 in enumerate(nums):
#                 if(i == j):
#                     continue
#                 if(num1 - num2 == k):
#                     judge = True
#                     for lis in my_list:
#                         if(lis[0] == num1 and lis[1] == num2):
#                             judge = False
#                             break
#                     if(judge == True):
#                         my_list.append([num1, num2])
#         num = len(my_list)
#         return num


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = collections.Counter(nums)
        print(c)
        count = 0
        if k < 0:
            return 0
        if k == 0:
            # 同じ物が2個以上存在した回数分+1
            # 重複は考えないので、何個同じものがきても+1でよい
            for item in c.keys():
                if c[item] > 1:
                    count += 1
            return count
        else:
            # 差がkの値しかifに入れない。
            for item in c.keys():
                if item + k in c:
                    count += 1
            return count


my_class = Solution()
# lst = list(int(i) for i in range(0, 9999)[::-1])
lst = list(map(int, input().split()))
print(lst)
K = 1
print(my_class.findPairs(lst, K))
