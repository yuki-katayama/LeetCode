class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s) - 1):
            if roman_numbers[s[i]] >= roman_numbers[s[i + 1]]:
                value += roman_numbers[s[i]]
            else:
                value -= roman_numbers[s[i]]
        value += roman_numbers[s[-1]]
        return value

solution = Solution()
print(solution.romanToInt("LVIII"))