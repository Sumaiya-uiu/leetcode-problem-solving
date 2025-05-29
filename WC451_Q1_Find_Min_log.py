class Solution(object):
    def minCuttingCost(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        if n <= k and m <= k:
            return 0  
    
        minCost = float('inf')
    
        
        if n > k:
            for i in range(1,n):
                part1 = i
                part2 = n - i
                if part1 <= k and part2 <= k and m <= k:
                    cost = part1 * part2
                    minCost = min(minCost, cost)
    
        
        if m > k:
            for i in range(1,m):
                part1 = i
                part2 = m - i
                if part1 <= k and part2 <= k and n <= k:
                    cost = part1 * part2
                    minCost = min(minCost, cost)
    

        return minCost
    
n = 4
m = 4
k = 6

solution = Solution()    
print(solution.minCuttingCost(n, m, k))

        