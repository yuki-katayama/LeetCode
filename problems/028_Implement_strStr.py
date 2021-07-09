# Not use methods
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         length_needle = len(needle)
#         if ((len(haystack) == 0 and len(needle) == 0) or len(needle) == 0):
#             return 0
#         if (len(haystack) == 0):
#             return -1
#         for i in range(len(haystack)):
#             if (haystack[i:length_needle + i] == needle):
#                 return i
#         return -1

# Use methods
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (needle in haystack):
            return haystack.index(needle)
        elif (len(needle) == 0 and len(haystack) == 0):
            return 0
        else:
            return -1

solution = Solution()
string = "hello"
needle = "ll"
print(solution.strStr(string, needle))