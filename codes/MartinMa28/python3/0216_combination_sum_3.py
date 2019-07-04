from copy import deepcopy

class Solution:
    def combinationSum3(self, k: int, n: int) -> list:
        def combination_backtrack(candidates: list, cur: list, ans: list) -> None:
            if cur == []:
                for num in candidates:
                    cur.append(num)
                    candidates.remove(num)
                
                    if len(cur) < k:
                        if sum(cur) > n:
                            candidates.append(cur.pop())
                            candidates.sort()
                            return
                        combination_backtrack(candidates, cur, ans)
                        candidates.append(cur.pop())
                        candidates.sort()
                    else:
                        # length of cur is equal to k
                        if sum(cur) >= n:
                            if sum(cur) == n:
                                ans.append(deepcopy(cur))

                            candidates.append(cur.pop())
                            candidates.sort()
                            return
                        else:
                            candidates.append(cur.pop())
                            candidates.sort()
                        
            else:
                for num in candidates:
                    if num > cur[-1]:
                        cur.append(num)
                        candidates.remove(num)
            
                        if len(cur) < k:
                            if sum(cur) > n:
                                candidates.append(cur.pop())
                                candidates.sort()
                                return

                            combination_backtrack(candidates, cur, ans)
                            candidates.append(cur.pop())
                            candidates.sort()
                        else:
                            # length of cur is equal to k
                            if sum(cur) >= n:
                                if sum(cur) == n:
                                    ans.append(deepcopy(cur))
                                candidates.append(cur.pop())
                                candidates.sort()
                                return
                            else:
                                candidates.append(cur.pop())
                                candidates.sort()


        cur = []
        ans = []
        combination_backtrack(list(range(1, 10)), cur, ans)

        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.combinationSum3(3, 7))