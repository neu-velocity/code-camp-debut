class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tempList = []
        candidates.sort()
        
        self.backtracking(candidates, target, res, tempList, 0)
        return res
    
    def backtracking(self, candidates, remain, res, tempList, start):
        if remain < 0:
            return
        elif remain == 0:
            res.append([i for i in tempList])
            
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    continue
                tempList.append(candidates[i])
                self.backtracking(candidates, remain - candidates[i], res, tempList, i)
                tempList.pop(-1)