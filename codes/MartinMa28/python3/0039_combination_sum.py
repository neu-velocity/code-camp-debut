from copy import deepcopy

class Solution:
    def combinationSum(self, candidate: list, target: int) -> list:
        def combination_sum_backtrack(candidate: list, cur: list, ans: list) -> None:
            if cur == []:
                for num in candidate:
                    cur.append(num)
                    if sum(cur) > target:
                        cur.pop()
                        return
                    elif sum(cur) == target:
                        ans.append(deepcopy(cur))
                        cur.pop()
                        return
                    else:
                        combination_sum_backtrack(candidate, cur, ans)
                        cur.pop()
            else:
                for num in candidate:
                    if num >= cur[-1]:
                        cur.append(num)
                        if sum(cur) > target:
                            cur.pop()
                            return
                        elif sum(cur) == target:
                            ans.append(deepcopy(cur))
                            cur.pop()
                            return
                        else:
                            combination_sum_backtrack(candidate, cur, ans)
                            cur.pop()



        ans = []
        cur = []
        combination_sum_backtrack(sorted(candidate), cur, ans)

        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.combinationSum([2, 3, 5], 8))