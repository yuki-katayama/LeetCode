
class Solution:
    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i-start)  # update the res
                # here should be careful, like "abba"
                print(dic[ch]+1, ch, res, start)
                print(dic)
                start = max(start, dic[ch]+1)
            dic[ch] = i
        # return should consider the last non-repeated substring
        return max(res, len(s)-start)


a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))
