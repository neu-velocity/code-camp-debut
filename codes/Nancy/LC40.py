class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        candidates.sort()
        self.backtracking(candidates, target, res, temp, 0)
        return res
    
    def backtracking(self, candidates, remain, res, temp, start):
        if remain == 0:
            res.append(temp)
        elif remain < 0:
            return
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    continue
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
            
                self.backtracking(candidates, remain - candidates[i], res, temp + [candidates[i]], i + 1)