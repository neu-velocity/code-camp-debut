class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 0:
            return []
        res = []
        #nums = [i for i in range(1,10)]
        
        def backtracking(curr, res, n, k, level):
            if n < 0:
                return
            if len(curr) == k and n == 0:
                res.append(curr)
                return
                            
            for num in range(level, 10):
                curr.append(num)
                backtracking(curr.copy(), res, n - num, k, num + 1)#make sure it's curr.copy() not curr!!!
                curr.remove(num)

                    
        backtracking([], res, n, k, 1)
        return res
                