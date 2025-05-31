class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if res > (INT_MAX - digit) // 10:
                return 0

            res = res * 10 + digit

        return sign * res
    
solution = Solution()
print(solution.reverse(120))

        