from typing import List

# Recursive runrime beats 84.85%
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wkyz"
		}
        res = []
        def recursive(pos, string, res):
            if pos == len(digits):
                if string != "":
                    res.append(string)
                return
            for c in num_dict[digits[pos]]:
                recursive(pos + 1, string + c, res)
        digits_len = len(digits)
        recursive(0, "", res)
        return res

# itertools runrime beats 99.18%
import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
		}
        l=[]
        if(len(digits) == 0):
            return l
        for i in digits:
            l.append(num_dict[i])
        #*lはアンパックされているイメージ
        s=list(itertools.product(*l))
        out=[]
        for i in s:
            out.append(''.join(list(i)))
        return out

solution = Solution()
print(solution.letterCombinations("56"))