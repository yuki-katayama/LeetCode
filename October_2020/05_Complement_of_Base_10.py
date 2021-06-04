class Solution:
    def bitwiseComplement(self, N: int) -> int:
        nums = bin(N)[2:]
        answer = []
        for n in nums:
            if(n == '1'):
                answer.append('0')
            else:
                answer.append('1')
        answer = ('').join(answer)
        return int(answer, 2)


a = Solution()
n = int(input())
for num in range(n):
    input_n = int(input())
    print(a.bitwiseComplement(input_n))
