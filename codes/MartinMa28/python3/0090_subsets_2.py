from copy import deepcopy

class Solution:
    def subsetsWithDup(self, nums: list) -> list:
        def _combination_backtrack(nums: list, used: list, cur: list, ans: list) -> None:
            if cur not in ans:
                ans.append(deepcopy(cur))
            else:
                return
            
            for i, num in enumerate(nums):
                if not used[i]:
                    if len(cur) == 0 or num >= cur[-1]:
                        cur.append(num)
                        used[i] = True
                        _combination_backtrack(nums, used, cur, ans)

                        cur.pop()
                        used[i] = False

        used = [False] * len(nums)
        cur = []
        ans = []
        _combination_backtrack(sorted(nums), used, cur, ans)
        
        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.subsetsWithDup([1, 2, 2]))