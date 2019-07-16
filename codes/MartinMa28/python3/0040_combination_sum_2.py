from copy import deepcopy

class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        def combination_backtrack(candidates: list, cur: list, ans: list) -> None:
            if cur == []:
                for num in sorted(set(candidates)):
                    cur.append(num)
                    candidates.remove(num)
                    if sum(cur) > target:
                        candidates.append(cur.pop())
                        candidates.sort()
                        return
                    elif sum(cur) == target:
                        ans.append(deepcopy(cur))
                        candidates.append(cur.pop())
                        candidates.sort()
                        return
                    else:
                        combination_backtrack(candidates, cur, ans)
                        candidates.append(cur.pop())
                        candidates.sort()
            else:
                for num in sorted(set(candidates)):
                    if num >= cur[-1]:
                        cur.append(num)
                        candidates.remove(num)
                        if sum(cur) > target:
                            candidates.append(cur.pop())
                            candidates.sort()
                            return
                        elif sum(cur) == target:
                            ans.append(deepcopy(cur))
                            candidates.append(cur.pop())
                            candidates.sort()
                            return
                        else:
                            combination_backtrack(candidates, cur, ans)
                            candidates.append(cur.pop())
                            candidates.sort()


        cur = []
        ans = []
        combination_backtrack(sorted(candidates), cur, ans)

        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.combinationSum2([8, 7, 4, 3], 11))
