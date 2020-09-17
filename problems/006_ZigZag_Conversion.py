class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows < 2):
            return s
        place = 0
        lines = [''] * numRows
        str_len = len(s)
        for i in range(str_len):
            if(i % (2 * numRows - 2) < numRows - 1):
                lines[place] += s[i]
                place += 1
            else:
                lines[place] += s[i]
                place -= 1
        return (''.join(lines))


my_class = Solution()
s1 = "PAYPALISHIRING"
numRows1 = 3
s2 = "PAYPALISHIRING"
numRows2 = 4
s3 = "radwimps,marshmello"
numRows3 = 5
s4 = "A"
numRows4 = 1
print(my_class.convert((s1), numRows1))
