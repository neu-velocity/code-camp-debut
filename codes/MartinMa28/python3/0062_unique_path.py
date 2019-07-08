import math

class Solution:
    def uniquePath(self, m: int, n: int) -> int:        
        # pick (n - 1) steps to go down out of (m - 1) + (n - 1) steps
        return int(math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1)))