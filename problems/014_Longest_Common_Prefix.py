from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        compare = strs[0]
        output = strs[0]
        for i in range(1, len(strs)):
            prefix = ""
            strs_len = len(strs[i])
            for j in range(len(compare)):
                if (j >= strs_len or compare[j] != strs[i][j]):
                    break
                prefix += strs[i][j]
            if (len(prefix) < len(output)):
                output = prefix
        return (output)

solution = Solution()
strs = ["dog","racecar","car"]
print(solution.longestCommonPrefix(strs))