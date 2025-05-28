class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {"I" : 1,"V" : 5,"X" : 10,"L" : 50, "C" : 100, "D" : 500, "M" : 1000}

        sum = 0
        prev_char_val = 0

        for char in reversed(s):
            value = roman_map[char]

            if value < prev_char_val:
                sum -= value
            else:
                sum += value
            
            prev_char_val = value
        
        return sum
    
solution = Solution()
print(solution.romanToInt("CIII")) 